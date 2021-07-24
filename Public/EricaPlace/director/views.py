from django.shortcuts import render,redirect, get_object_or_404
from rsv.models import Reservation
from main.models import College, Building, Room, College
from faq.models import FAQ
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import timedelta, datetime
from django.contrib import messages
from django.core.mail.message import EmailMessage

# Create your views here.
def login(request):
  if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #auth.authenticate 라는 말은 DB에서 방금전에 입력한 이 내용이 우리한테 있는 회원명단이 맞는지 확인시켜주는 함수
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:    # is not None = None이 아니라면 = 회원이라면
            auth.login(request,user)
            return redirect('director_status')
        else:
            return render(request, 'director_login.html', {'error': 'username or password is incorrect'})
  else:
        return render(request, 'director_login.html')

def logout(request):
  if request.user.is_authenticated:
    auth.logout(request)
  return redirect('main')

def status(request):
  college = College.objects.all()
  reservation = Reservation.objects.all()
  search_status = {}
  now = datetime.now()
  formatednow = now.strftime("%Y-%m-%d")
  if 'college' in request.GET:
    colNumber = request.GET.get('college')
    search_status['college'] = colNumber
    if(colNumber != ""): reservation = reservation.filter(room_id__college__id = colNumber)
  
  if 'admit' in request.GET:
    Admit = request.GET.get('admit')
    search_status['admit'] = Admit
    if(Admit != ""): reservation = reservation.filter(admit = Admit)

  if 'start_date' in request.GET:
    start_date = request.GET.get('start_date')
    search_status['start_date'] = start_date
    if(start_date != ""): reservation = reservation.filter(rsv_date__gte = start_date)

  if 'end_date' in request.GET:
    end_date = request.GET.get('end_date')
    search_status['end_date'] = end_date
    if(end_date != ""):
      # end_date = datetime.strptime(end_date, "%Y-%m-%d")
      # end_date += timedelta(days=1)
      # end_date = end_date.strftime("%Y-%m-%d")
      reservation = reservation.filter(rsv_date__lte = end_date)

  reservation = reservation.order_by('-date')
  for rsv in reservation:
    rsv.end_time += 1
  rsv_paginator = Paginator(reservation, 4)

  page = request.GET.get('page')
  page_list = request.GET.get('pagelist')
  page_num_list = []
  if(rsv_paginator.count > 0):
    for i in rsv_paginator.page_range:
      page_num_list.append(i)

  page_num_list_paginator = Paginator(page_num_list,5)

  posts = rsv_paginator.get_page(page)
  pagelist = page_num_list_paginator.get_page(page_list)

  contents = {
    "posts" : posts,
    "pagelists" : pagelist,
    "college" : college,
    "search_status" : search_status,
    "now": formatednow,
  }

  return render(request, 'director_status.html', contents)

def send_email(msg, email):
  subject = "[EricaPlace] 대관 신청 통보 메시지"
  to = [email]
  from_email = 'ericaplace2@gmail.com'
  message = msg
  EmailMessage(subject=subject,
  body=message,
  to=to,
  from_email=from_email).send()

def rsv_admit(request, rsv_id, type):
  rsv = get_object_or_404(Reservation, pk = rsv_id)

  rsv_start = rsv.start_time
  rsv_end = rsv.end_time

  path = ''
  if 'pagelist' in request.GET:
    pagelist = request.GET.get('pagelist')
    path += ('?pagelist=' + pagelist)
  if 'page' in request.GET:
    page = request.GET.get('page')
    path += ('&page=' + page)
  if 'college' in request.GET:
    colNumber = request.GET.get('college')
    path += ('&college=' + colNumber)
  if 'admit' in request.GET:
    Admit = request.GET.get('admit')
    path += ('&admit=' + Admit)
  if 'start_date' in request.GET:
    start_date = request.GET.get('start_date')
    path += ('&start_date=' + start_date)
  if 'end_date' in request.GET:
    end_date = request.GET.get('end_date')
    path += ('&end_date=' + end_date)

  if type == 1:
    info = Reservation.objects.all().filter(rsv_date = rsv.rsv_date, room_id = rsv.room_id, admit=1, start_time__lte = rsv_end, end_time__gte = rsv_start).values('start_time','end_time')

    if info:
      messages.error(request, '승인이 거부되었습니다. 사유 : 예약시간 중복')
      return redirect('/director/status'+path)

  rsv.admit = type
  rsv.save()

  rsv_date = rsv.rsv_date.strftime("%Y-%m-%d")
  
  msg = rsv.username + "\n"
  msg += rsv.room_id.name + "\n"
  msg += rsv_date + "\n"
  msg += str(rsv.start_time) + ":00 ~ " + str(rsv.end_time+1) + ":00\n"

  if type == 1:
    msg += "대관 신청이 승인되었습니다."

  elif type == 0:
    msg += "대관 신청 승인이 취소되었습니다. (승인 보류)\n"
    message = request.GET.get('message')
    msg += "사유 : " + message

  elif type == 2:
    msg += "대관 신청 승인이 거부되었습니다."
    message = request.GET.get('message')
    msg += "사유 : " + message

  email = rsv.email
  send_email(msg, email)

  return redirect('/director/status'+path)

def modify(request):
  return render(request, 'modify.html')

def modify_building(request):
  buildings = Building.objects
  return render(request, 'modify_building.html', {'buildings':buildings})

def modify_faq(request):
  faqs = FAQ.objects.all()
  faqlist = {}
  index = 1
  for faq in faqs:
    faqlist[faq]=index
    index+=1
  return render(request, 'modify_faq.html', {'faqs':faqlist})

def modify_room(request, building_id):
  rooms = Room.objects.filter(building = building_id)
  building = get_object_or_404(Building, pk = building_id)
  return render(request, 'modify_room.html', {'rooms' : rooms, 'building':building})

def building_list(request):
  buildings = Building.objects
  return render(request, 'building_list.html', {'buildings':buildings})

def create_room(request, building_id):
  building = get_object_or_404(Building, pk = building_id)
  colleges = College.objects
  if request.method == "POST":
    room = Room()
    room.name = request.POST["name"]
    room.subname = request.POST["subname"]
    room.capacity = int(request.POST["capacity"])
    room.photo = request.FILES.get('photo')
    room.equipment = request.POST["equipment"]
    college_id = int(request.POST['college'])
    room.college = colleges.get(id = college_id)

    room.building = building
  
    room.save()
    messages.info(request, '생성이 완료되었습니다.')
    return redirect("modify_room", building.id)

  
  return render(request, 'create_room.html', {'building':building, 'colleges':colleges})

def update_room(request, room_id):
  room = get_object_or_404(Room, pk = room_id)
  colleges = College.objects
  if request.method == "POST":
    room.name = request.POST["name"]
    room.subname = request.POST["subname"]
    room.capacity = int(request.POST["capacity"])
    for img in request.FILES.getlist('photo'):
      room.photo = img
    room.equipment = request.POST["equipment"]
    college_id = int(request.POST['college'])
    room.college = colleges.get(id = college_id)
    room.save()
    messages.info(request, '수정이 완료되었습니다.')
    return redirect("modify_room", room.building.id)

  contents = {
    "room" : room,
    "building" : room.building,
    "college" : room.college,
    "colleges" : colleges
    }
  return render(request, 'update_room.html', contents)

def create_building(request):
  if request.method == "POST":
    building = Building()
    building.name = request.POST["name"]
    building.english_name = request.POST["english_name"]
    building.photo = request.FILES.get('photo')
    building.code = request.POST["code"]
    building.save()
    messages.info(request, '생성이 완료되었습니다.')
    return redirect('modify_building')
  return render(request, 'create_building.html')

def update_building(request, building_id):
  building = get_object_or_404(Building, pk = building_id)
  if request.method == "POST":
    building.name = request.POST["name"]
    building.english_name = request.POST["english_name"]
    for img in request.FILES.getlist('photo'):
      building.photo = img
    building.code = request.POST["code"]
    building.save()
    messages.success(request, "수정되었습니다.")
    return redirect('modify_building')
  return render(request, 'update_building.html',{'building':building})

def create_question(request):
  if request.method == "POST":
    faq = FAQ()
    faq.title = request.POST['title']
    faq.writer = "관리자"
    faq.date = datetime.now()
    faq.content = request.POST['content']
    faq.save()
    messages.success(request, "게시글이 작성 되었습니다.")
    return redirect('modify_faq')
  return render(request, 'create_question.html')

def update_question(request,faq_id):
  faq = get_object_or_404(FAQ, pk = faq_id)
  if request.method == "POST":
    faq.title = request.POST['title']
    faq.content = request.POST['content']
    faq.save()
    messages.success(request, "게시글이 수정 되었습니다.")
    return redirect('modify_faq')
  else:
    contents = {
    'id' : faq.id,
    'title' : faq.title,
    'content' : faq.content
    }
    return render(request, 'update_question.html', contents)

def delete_room(request, room_id):

  room = get_object_or_404(Room, id = room_id)
  building = room.building.id
  room.delete()
  messages.success(request, "방이 삭제되었습니다.")
  return redirect('modify_room', building)

def delete_building(request, building_id):

  building = get_object_or_404(Building, id = building_id)
  building.delete()
  messages.success(request, "건물이 삭제되었습니다.")
  return redirect('modify_building')

def delete_faq(request, faq_id):
  faq = FAQ.objects.get(id = faq_id)
  faq.delete()
  messages.success(request, "게시글이 삭제 되었습니다.")
  return redirect('modify_faq')
from django.shortcuts import render, get_object_or_404,redirect # import 필요!
from main.models import Room
from .models import Reservation, Purpose
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from json import dumps
from django.contrib import messages
import re
from django.core.mail.message import EmailMessage
import random

### 정규표현식(Regular Expression) ###
def Regular_expression(name, email, phone, user):
  #이름
  p1 = re.compile("^[가-힣]+$|^[a-zA-Z]+\s[a-zA-Z]+$")
  if not p1.match(name): return False
  #이메일
  p2 = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")
  if not p2.match(email): return False
  #전화번호
  p3 = re.compile("^\d{11}$")
  if not p3.match(phone): return False
  #학번 or 사업자번호
  if user == None: return True
  p4 = re.compile("^\d{10}$")
  if not p4.match(user): return False
  return True



# Create your views here.
def reservation(request, room_id):
  room_detail = get_object_or_404(Room, pk = room_id)
  now = datetime.now()
  formatednow = now.strftime("%Y-%m-%d")
  info = Reservation.objects.all().order_by('rsv_date').filter(room_id = room_id, admit=1).values('rsv_date','start_time','end_time')
  dateinfo = {}
  for date in info:
    rsv_date = date['rsv_date']
    start = date['start_time']
    end = date['end_time']
    
    date = rsv_date.strftime("%Y-%m-%d")

    if date in dateinfo:
      dateinfo[date].append((start,end))
    else:
      dateinfo[date] = [(start,end)]
  dataJSON = dumps(dateinfo)
  return render(request, 'reservation.html', {'room' : room_detail,'now':formatednow, 'dateinfo':dataJSON} )
  
def rsv_status(request):
  return render(request, 'login.html')

def form(request, room_id):
    if request.method == 'POST':
      timelist = request.POST.getlist('chk')
      start = timelist[0]
      end = int(timelist[-1])+1
      room_detail = get_object_or_404(Room, pk = room_id)
      date = request.POST['date']
    purposes = Purpose.objects

    contents =  {'room':room_detail, 'start_time':start , 'end_time':end, 'purposes':purposes, 'date':date }
    return render(request, 'form.html' ,contents)

def send_email(msg, email):
  subject = "[EricaPlace] 대관 신청 통보 메시지"
  to = [email]
  from_email = 'ericaplace2@gmail.com'
  message = msg
  EmailMessage(subject=subject,
  body=message,
  to=to,
  from_email=from_email).send()

@csrf_exempt
def create(request):
  EmptyForm = False

  if request.method == 'POST' and 'start' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'end' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'date' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'room' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'NAME' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'MAN_NUM' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'COMPANY' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'list' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'PURPOSE' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'PHONE_NUM' not in request.POST:
    EmptyForm = True
  elif request.method == 'POST' and 'EMAIL' not in request.POST:
    EmptyForm = True

  if request.method == 'POST' and 'list' in request.POST:
    user_type = request.POST['list']
    if(user_type == "0"): EmptyForm = True
    elif(user_type == "1"):
      if request.method == 'POST' and 'STUDENT_ID' not in request.POST:
        EmptyForm = True
    elif(user_type == "3"):
      if request.method == 'POST' and 'COM_NUM' not in request.POST:
        EmptyForm = True

  if request.method == 'POST' and 'PURPOSE' in request.POST:
    if(request.POST['PURPOSE'] == "-"): EmptyForm = True
  
  if request.method == 'POST' and 'MAN_NUM' in request.POST:
    if(request.POST['MAN_NUM'] == "0"): EmptyForm = True

  if EmptyForm:
    messages.error(request, "잘못된 접근입니다.")
    return redirect("main")

  # 여기까지 통과했으면 request.POST[]로 모두 오류없이 접근 가능.
  rsv = Reservation()
  room_index = int(request.POST['room'])

  if request.method == 'POST' and 'STUDENT_ID' in request.POST:
    user_num = request.POST['STUDENT_ID']
  elif request.method == 'POST' and 'COM_NUM' in request.POST:
    user_num = request.POST['COM_NUM']
  else: #관계자
    user_num = None
  

  if not Regular_expression(request.POST['NAME'],request.POST['EMAIL'],request.POST['PHONE_NUM'], user_num):
    messages.error(request, "잘못된 접근입니다.")
    return redirect("rsv", room_index)


  info = Reservation.objects.all().filter(rsv_date = request.POST['date'], room_id = room_index, admit=1, start_time__lte = int(request.POST['end'])-1, end_time__gte = int(request.POST['start'])).values('start_time','end_time')
  if info:
    messages.error(request, '승인이 거부되었습니다. 사유 : 예약시간 중복')
    return redirect("rsv", room_index)

  rsv.room_id = Room.objects.get(id=room_index)
  rsv.start_time = int(request.POST['start'])
  rsv.end_time = int(request.POST['end'])-1
  rsv.rsv_date = request.POST['date']
  rsv.headcount = int(request.POST['MAN_NUM'])
  rsv.user_type = request.POST['list']
  rsv.username = request.POST['NAME']
  rsv.group_name = request.POST['COMPANY']

  if request.method == 'POST' and 'STUDENT_ID' in request.POST:
    rsv.user_number = request.POST['STUDENT_ID']
  elif request.method == 'POST' and 'COM_NUM' in request.POST:
    rsv.user_number = request.POST['COM_NUM']

  purpose_index = int(request.POST['PURPOSE'])
  rsv.purpose = Purpose.objects.get(id=purpose_index)

  rsv.phone_number = request.POST['PHONE_NUM']
  rsv.email = request.POST['EMAIL']

  rsv.admit = False
  code = random.randrange(100000,1000000)
  rsv.authentic_code = code
  rsv.save()

  rsv_date = rsv.rsv_date
  msg = rsv.username + "\n"
  msg += rsv.room_id.name + "\n"
  msg += rsv_date + "\n"
  msg += str(rsv.start_time) + ":00 ~ " + str(rsv.end_time+1) + ":00\n"
  
  msg += "인증코드 : " + str(code) + "\n"
  email = rsv.email
  send_email(msg, email)

  messages.info(request, '신청이 완료되었습니다. \\n신청 승인 시 승인 이메일이 발송되니 확인해주세요. \\n신청 취소 시 필요한 인증코드는 이메일을 확인해주세요.')


  return redirect('/')
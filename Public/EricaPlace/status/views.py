from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rsv.models import Reservation
from django.contrib import messages

# Create your views here.
def status(request):
  return render(request, 'login.html')

@csrf_exempt
def status_list(request):
  
  name = request.POST['name']
  phone = request.POST['phone']
  reservation = Reservation.objects.all().filter(
    username = name,
    phone_number = phone,
  )
  reservation = reservation.order_by('-date')

  for rsv in reservation:
    rsv.end_time += 1

  content = {"reservation" : reservation}

  if not reservation:
    messages.warning(request, '일치하는 정보가 없습니다.')
    return redirect('status')
  return render(request, 'status.html', content)

def remove(request, rsv_id):
  rsv = Reservation.objects.get(id = rsv_id)
  code = request.POST['code']

  if not code.isdigit():
    messages.info(request, '인증 번호가 일치하지 않습니다.')

  elif(int(code) == rsv.authentic_code):
    rsv.delete()
    messages.info(request, '신청 취소가 완료되었습니다.')

  else:
    messages.info(request, '인증 번호가 일치하지 않습니다.')

  name = rsv.username
  phone = rsv.phone_number
  reservation = Reservation.objects.all().filter(
    username = name,
    phone_number = phone,
  )

  reservation = reservation.order_by('-date')
  content = {"reservation" : reservation}
  return render(request, 'status.html', content)
from django.shortcuts import get_object_or_404, render
from .models import Room, Contacts, Building
from rsv.models import Reservation, Purpose

# Create your views here.

def main(request):
  rooms = []
  rooms.append(get_object_or_404(Room, name="1공학관 304"))
  rooms.append(get_object_or_404(Room, name="4공학관 106"))
  rooms.append(get_object_or_404(Room, name="과학기술관 103"))
  rooms.append(get_object_or_404(Room, name="잔디축구장"))
  rooms.append(get_object_or_404(Room, name="클러스터 506"))
  rooms.append(get_object_or_404(Room, name="Lion's Hall"))

  contents = {'rooms' : rooms}

  return render(request, 'main.html', contents)

def useGuide(request):

  contacts = Contacts.objects.all()
  contents = {}

  for contact in contacts:
    category = contact.category
    if not category in contents:
      contents[category]=[]
    contents[category].append([contact.building_name, contact.phone_number])
  
  return render(request, 'useGuide.html', {'contents' : contents})

def mainplace(request):
  rooms = []
  rooms.append(get_object_or_404(Room, name="1공학관 304"))
  rooms.append(get_object_or_404(Room, name="4공학관 106"))
  rooms.append(get_object_or_404(Room, name="과학기술관 103"))
  rooms.append(get_object_or_404(Room, name="잔디축구장"))
  rooms.append(get_object_or_404(Room, name="클러스터 506"))
  rooms.append(get_object_or_404(Room, name="Lion's Hall"))

  contents = {'rooms' : rooms}

  return render(request, 'mainplace.html',contents)

def building(request):
  buildings = Building.objects
  return render(request, 'building.html', {'buildings':buildings})


def roomlist(request, building_id):
  roomlist = Room.objects.filter(building = building_id)

  return render(request, 'roomlist.html', {'roomlist' : roomlist})

def headcount(request, count):
  if count == 20:
    rooms = Room.objects.filter(capacity__lt = count)
    headcount = "20명 미만"
  elif count == 51:
    rooms = Room.objects.filter(capacity__gte = count)
    headcount = "50명 이상"
  else:
    rooms = Room.objects.filter(capacity__lt = count , capacity__gte = count-10)
    headcount = str(count-10) + " ~ " + str(count-1)+"명"

  return render(request, 'headcount.html', {'rooms':rooms, 'headcount':headcount})

def recommend(request, purpose_id):
  rsv = Reservation.objects.filter(purpose = purpose_id, admit = 1).values('room_id')

  rooms = {}
  for entry in rsv:
    room_id = entry['room_id']
    if not room_id in rooms:
      room = get_object_or_404(Room, pk = room_id)
      rooms[room_id] = [room,0]
    rooms[room_id][1] += 1

  sorted_rooms = sorted(rooms.items(), reverse=True, key=lambda x: x[1][1])

  purpose = get_object_or_404(Purpose, pk = purpose_id)
  return render(request, 'recommend.html', {"rooms":sorted_rooms, "purpose":purpose})
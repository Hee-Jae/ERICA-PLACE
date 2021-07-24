from django.shortcuts import get_object_or_404
from main.models import Room, Building

def totalmenu(request):
  rooms = []
  rooms.append(get_object_or_404(Room, name="1공학관 304"))
  rooms.append(get_object_or_404(Room, name="4공학관 106"))
  rooms.append(get_object_or_404(Room, name="과학기술관 103"))
  rooms.append(get_object_or_404(Room, name="잔디축구장"))
  rooms.append(get_object_or_404(Room, name="클러스터 506"))
  rooms.append(get_object_or_404(Room, name="Lion's Hall"))

  buildings = Building.objects
  content = {'mainplace' : rooms, 'buildings' : buildings}
  return content


def search(request):
  rooms = Room.objects
  roomlist = {}
  roomlist['twenty'] = rooms.filter(capacity__lt = 20)
  roomlist['thirty'] = rooms.filter(capacity__lt = 30, capacity__gte = 20)
  roomlist['fourty'] = rooms.filter(capacity__lt = 40, capacity__gte = 30)
  roomlist['fifty'] = rooms.filter(capacity__lt = 50, capacity__gte = 40)
  roomlist['fifty_one'] = rooms.filter(capacity__gte = 50)
  return roomlist

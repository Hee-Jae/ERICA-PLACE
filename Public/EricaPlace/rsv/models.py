from django.db import models
from django.db.models.deletion import CASCADE
from main.models import Room



# Create your models here.
class Purpose(models.Model):
    use_purpose = models.TextField()

    def __str__(self):
        return self.use_purpose

class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=CASCADE)
    rsv_date = models.DateField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    headcount = models.IntegerField()   # 인원수
    user_type = models.IntegerField()
    username = models.CharField(max_length=90)
    group_name = models.CharField(max_length=80, null=True)
    
    user_number = models.CharField(max_length=15,null = True) #학번 or 사업자번호

    purpose = models.ForeignKey(Purpose, on_delete=CASCADE)
    
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(default='')

    admit = models.IntegerField(default = 0) #예약승인여부

    date = models.DateTimeField(auto_now_add=True, blank=True) #예약 시간
    authentic_code = models.IntegerField(default=100000)

    def __str__(self):
        return '['+self.room_id.name+'] ' + self.username
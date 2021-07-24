from django.db import models
from datetime import datetime
# Create your models here.
class FAQ(models.Model):
  title = models.CharField(max_length=100)
  writer = models.CharField(max_length=45)
  date = models.DateField(default=datetime.now, blank=True)
  content = models.TextField()

  def __str__(self):
    return self.title
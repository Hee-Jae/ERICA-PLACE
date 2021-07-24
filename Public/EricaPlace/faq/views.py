from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq(request):
  faqs = FAQ.objects.all()
  count = FAQ.objects.all().count()
  faqlist = {}
  index = 1
  for faq in faqs:
    faqlist[faq]=index
    index+=1
  return render(request, 'faq.html', {'faqs':faqlist, 'count':count})
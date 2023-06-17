from django.http import HttpResponse
from django.shortcuts import render
from . models import  place
from . models import  feedback
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=feedback.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})


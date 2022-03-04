from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
  now=datetime.datetime.now()
  return render(request,"newyear/index.html",{
    "newyear":now.month==3 and now.day==3
  })
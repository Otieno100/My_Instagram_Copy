from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import  Image

# Create your views here.
def index(request):
    return render(request,'index.html')



def profile(request):
    date = dt.date.today()
    profile = Image.profile()
    return render(request, 'instagram/profile.html', {"date": date,"post":profile})

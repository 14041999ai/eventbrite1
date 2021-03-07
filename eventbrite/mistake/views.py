from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Event
def upload(request):
    return render(request, 'index.html')

def display(request):
    date = (request.GET.get('bdate','default'))
    time = (request.GET.get('time','default'))
    vname = (request.GET.get('vname','default'))
    address = (request.GET.get('address','default'))
    img = (request.GET.get('img','default'))
    print(address)
    
    event = Event(date=date, time=time, vname=vname, address=address, img=img)
    event.save()
    print(event)
   
    return render(request, 'eventbrite.html')
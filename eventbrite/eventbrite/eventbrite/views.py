from django.http import HttpResponse
from django.shortcuts import render


def upload(request):
    return render(request, 'index.html')


from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def hima(request):
    return HttpResponse('hima is good girl')
def kanna(request):
    return HttpResponse('<h1><button> good boy</button></h1>')   

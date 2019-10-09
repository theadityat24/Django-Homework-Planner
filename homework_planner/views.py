from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def assignments(request):
    return HttpResponse("<i>My first website print</i>")

def classWork(request):
    return HttpResponse("<button>classWork</button>")

def ultraSecret(request):
    return HttpResponse("This is a very secret server wow u accesed it!")
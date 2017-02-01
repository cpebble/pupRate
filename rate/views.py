from django.shortcuts import render
from .models import Pupper

# Create your views here.
def about(request):
    return render(request, "rate/about.html", locals())

def rate(request):
    return render(request, "rate/rate.html", locals())

def pup(request):
    pup = Pupper.objects.order_by('?')[0]
    return render(request, "rate/pup.html",locals() )

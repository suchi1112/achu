from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import person
# Create your views here.
def demo(request):
    obj=place.objects.all()
    objj=person.objects.all()
    return render(request,"index.html",{'result':obj,'res':objj})



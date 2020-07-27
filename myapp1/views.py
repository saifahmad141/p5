from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def child(request):
    return render(request,"child.html")
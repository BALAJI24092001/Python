from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def __hello__(request):
    x = 1
    y = 2
    return render(request, "hello.html", {'name': "Balaji"})

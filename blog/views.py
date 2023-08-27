from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return render(request, 'blog/base.html')


def loginn(request):
    return render(request, 'blog/loginn.html')


def signup(request):
    return render(request, 'blog/signup.html')
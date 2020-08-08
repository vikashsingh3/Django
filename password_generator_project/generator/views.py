from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    mypassword = 'testing'
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharacter'):
        characters.extend(list('~!@#$%^&*()_+=-;:<>?/.,'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def aboutus(request):
    msg = "Welcome to my new page. I am learning Django 3."
    return render(request, 'generator/aboutus.html', {'about':msg})
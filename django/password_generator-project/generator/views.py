"""
This is the views page where all the routes are present
"""

import random
from django.shortcuts import render

# Create your views here.


def home(request):
    """
    this is the home page where you can select parameters to generate a password
    :param request:
    :return: HTML page
    """
    return render(request, "generator/home.html")


def password(request):
    """
    this is the password page where the password is generated and displayed on the screen
    :param request:
    :return: HTML page
    """
    characters = list("abcdefghijklmnopqrstuvxyz")
    if request.GET.get("uppercase"):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get("special"):
        characters.extend("~!@#$%^&*()")
    if request.GET.get("numbers"):
        characters.extend("1234567890")
    the_password = ""
    length = int(request.GET.get("length", 12))
    loop_length = 0
    while loop_length < length:
        the_password += random.choice(characters)
        loop_length += 1

    return render(request, "generator/password.html", {"password": the_password})

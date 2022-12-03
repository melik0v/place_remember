# from django.views.generic import ListView
# from models import Memory

from django.shortcuts import render

links_dict = {"main": "index.html", "login": "logging_page.html"}


def show_main_page(request):
    return render(request, "users/index.html")

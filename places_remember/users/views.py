from django.shortcuts import render


def show_login_page(request):
    return render(request, 'logging_page.html')

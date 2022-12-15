from django.shortcuts import render, redirect


def show_login_page(request):
    if request.user.is_authenticated:
        return redirect("memories:memories")
    return render(request, "login_page.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import ContactForm

def home(request):
    return render(request, "home.html")


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")
    return render(request, "login.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    return render(request, "logout.html")


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    return render(request, "register.html", {"form": form})


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)  # Or save to DB
        return render(request, "contact.html", {"form": ContactForm(), "msg": "Message Sent!"})
    return render(request, "contact.html", {"form": form})

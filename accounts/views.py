from django.contrib.auth import login
from django.shortcuts import redirect, render

from accounts.forms import SignupForm


def home(request):
    return render(request, "home.html")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})

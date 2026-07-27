from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import path
from django.views.generic import CreateView, TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class SignupForm(UserCreationForm):
    display_name = forms.CharField(max_length=150, required=True)

    class Meta(UserCreationForm.Meta):
        fields = ("username",)

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.first_name = self.cleaned_data["display_name"]
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = "/"

    def form_valid(self, form):
        super().form_valid(form)
        login(self.request, self.object)
        return HttpResponseRedirect(self.success_url)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignupView.as_view(), name="signup"),
]

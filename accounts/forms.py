from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    display_name = forms.CharField(
        max_length=150,
        label="Display name",
        help_text="Shown to your team.",
    )

    class Meta:
        model = User
        fields = ["username", "display_name", "password1", "password2"]

    def clean_display_name(self):
        value = self.cleaned_data["display_name"].strip()
        if not value:
            raise forms.ValidationError("Display name is required.")
        return value

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["display_name"]
        if commit:
            user.save()
        return user

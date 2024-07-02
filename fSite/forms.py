from django import forms
from .models import Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'about']

        def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            self.fields['image'].widget.attrs.update({'class': 'form-control'})
            self.fields['about'].widget.attrs.update({'class': 'form-control'})


# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']
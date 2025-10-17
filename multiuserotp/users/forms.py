from django.contrib.auth.forms import UserCreationForm

from users.models import Customuser

from django import forms


class SignupForm(UserCreationForm):
    role_choices=(('student','Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=role_choices)
    gender_choices=(('male','Male'),('female','Female'))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    class Meta:
        model=Customuser
        fields=['username','password1','password2','email','first_name','last_name','phone','role','gender']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

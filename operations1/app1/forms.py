from django import forms
from django.forms import RadioSelect


class Additionform(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class Bmi(forms.Form):
    weight=forms.FloatField()
    height=forms.FloatField()

class Signup(forms.Form):
    gender_choices=(('male','MALE'),('female','FEMALE'))
    role_choices=(('admin','ADMIN'),('student','STUDENT'))
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    place=forms.CharField()
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    email=forms.EmailField()

class Calc(forms.Form):
    activity_choices=((1,'sedentary'),
                      (1.375,'lightly active'),
                        (1.75,'moderative active'),
                      (1.9,'extra active'))
    gender_choices=(('male','MALE'),('female','FEMALE'))

    weight = forms.IntegerField()
    height = forms.IntegerField()
    age=forms.IntegerField()
    activity_levels=forms.ChoiceField(choices=activity_choices)
    gender=forms.ChoiceField(choices=gender_choices,widget=RadioSelect)


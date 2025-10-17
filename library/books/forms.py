from django import forms
from books.models import Book


# class Bookform(forms.Form):
#
#     title=forms.CharField()
#     author=forms.CharField()
#     pages=forms.IntegerField()
#     price=forms.IntegerField()
#     language=forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
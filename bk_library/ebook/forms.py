from django import forms
from .models import EBooksModel


class UploadBookForm(forms.ModelForm):
    class Meta:
        model = EBooksModel
        fields = "__all__"

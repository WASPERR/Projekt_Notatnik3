from django import forms
from .models import Note

class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['tytul', 'tresc', 'priorytet']
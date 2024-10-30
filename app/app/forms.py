from django import forms
from .models import Note  # Импортируйте вашу модель Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # Укажите поля, которые хотите включить в форму

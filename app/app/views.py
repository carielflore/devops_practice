from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Note  # Замените Note на вашу модель
from .forms import NoteForm

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'  # Убедитесь, что у вас есть соответствующий шаблон

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'  # Убедитесь, что у вас есть соответствующий шаблон
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'  # Убедитесь, что у вас есть соответствующий шаблон
    success_url = reverse_lazy('note_list')  # Перенаправление на список заметок после успешного создания

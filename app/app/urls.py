from django.contrib import admin  # Добавьте эту строку
from django.urls import path
from django.views.generic import RedirectView
from .views import NoteListView, NoteDetailView, NoteCreateView  # Убедитесь, что у вас есть правильные импорты ваших представлений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='notes/')),  # Перенаправление на 'notes/' при доступе к корню
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/new/', NoteCreateView.as_view(), name='note_create'),  # Новый маршрут для создания заметки
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]

from django.urls import path
from .views import NoteListAPIView, NoteDetailAPIView

app_name = 'notes'

urlpatterns = [
    path('notes/', NoteListAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail'),
]

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    NOTE_TYPES = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

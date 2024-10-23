from django.db import models
from django.contrib.auth.models import User

# Model for Notes
class Note(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to Django's built-in User model

    def __str__(self):
        return self.title or "Untitled"

# Model for Tags
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Model for the Many-to-Many relationship between Notes and Tags
class NoteTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('note', 'tag')

    def __str__(self):
        return f'{self.note.title} - {self.tag.name}'
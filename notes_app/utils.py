from .models import Note

def verify_note_belongs_to_user(note_id: int, user_id: int) -> bool:
    note = Note.objects.filter(id=note_id, user_id=user_id).first()
    return note is not None
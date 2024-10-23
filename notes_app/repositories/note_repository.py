from ..models import Note, Tag

def get_notes_by_user(user_id: int) -> list:
    return Note.objects.filter(user_id=user_id)

def get_notes_by_tag(tag_name: str) -> list:
    tag = Tag.objects.filter(name=tag_name).first()
    if tag:
        return Note.objects.filter(notetag__tag=tag)
    return []

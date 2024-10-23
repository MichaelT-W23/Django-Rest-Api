from notes_app.models import Tag
from notes_app.repositories.note_repository import get_notes_by_tag, get_notes_by_user


def fetch_notes_by_user(user_id: int) -> list:
    notes = get_notes_by_user(user_id)
    return [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]


def fetch_notes_by_tag(tag_name: str) -> list:
    notes = get_notes_by_tag(tag_name)
    return [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]


def get_all_tags_from_users_notes(user_id: int) -> list:
    notes = get_notes_by_user(user_id)
    tags = set()

    for note in notes:
        note_tags = Tag.objects.filter(notetag__note=note)
        for tag in note_tags:
            tags.add(tag.name)
    
    return list(tags)

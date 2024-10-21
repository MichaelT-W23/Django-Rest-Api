from django.contrib.auth.models import User
from django.db import IntegrityError

def create_user(username: str, email: str, password: str) -> User:
    try:
        new_user = User.objects.create_user(username=username, email=email, password=password)
        return new_user
    except IntegrityError as e:
        raise e


def get_user_by_username(username: str) -> User:
    return User.objects.filter(username=username).first()


def get_all_db_users():
    try:
        users = User.objects.filter(is_superuser=False)
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    except Exception as e:
        raise e
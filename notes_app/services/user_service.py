from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from ..exceptions import InvalidCredentialsError
from ..forms import UserForm

def add_user(data: dict) -> dict:
    form = UserForm(data)
    
    if form.is_valid():
        user_data = form.cleaned_data
        if get_user_by_username(user_data['username']):
            return {'error': 'Username already exists'}

        try:
            user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'])

            refresh = RefreshToken.for_user(user)

            response = {
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return response

        except IntegrityError:
            return {'error': 'Unable to create user'}
    else:
        return {'error': form.errors}


def sign_in_user(username: str, password: str) -> dict:
    user = get_user_by_username(username)

    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        
        response = {
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return response
    else:
        return {'error': 'Invalid credentials'}
    

def get_user(username: str) -> dict:
    user = get_user_by_username(username)
    
    if user:
        return {"id": user.id, "username": user.username, "email": user.email}
    else:
        raise InvalidCredentialsError()


def get_user_by_username(username: str) -> User:
    return User.objects.filter(username=username).first()

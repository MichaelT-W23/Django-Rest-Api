from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..services.note_service import fetch_notes_by_tag, fetch_notes_by_user, get_all_tags_from_users_notes
from ..services.user_service import add_user, sign_in_user, get_user
from ..permissions import IsAdminUser
from django.db import connection
from ..repositories.user_repository import get_all_db_users
from rest_framework import status


@api_view(['GET'])
def home_page(request):
    return JsonResponse('Hello from your Django Rest Api', safe=False)


@api_view(['GET'])
def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            db_uri = connection.settings_dict['NAME']
            return JsonResponse(f'Connection successful! Database URI: {db_uri}', safe=False)
    except Exception as e:
        return JsonResponse(f'Error: {str(e)}', safe=False)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_users(request):
    try:
        users_list = get_all_db_users()
        return JsonResponse(users_list, status=status.HTTP_200_OK, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def register_user(request):
    try:
        user_response = add_user(request.data)
        
        if 'error' in user_response:
            return JsonResponse(user_response, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(user_response, status=status.HTTP_201_CREATED)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login_user(request):
    try:
        login_response = sign_in_user(request.data['username'], request.data['password'])
        
        if 'error' in login_response:
            return JsonResponse(login_response, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(login_response, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_notes_by_user(request, user_id):
    try:
        notes = fetch_notes_by_user(user_id)
        return JsonResponse(notes, status=status.HTTP_200_OK, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_notes_by_tag(request, tag_name):
    try:
        notes = fetch_notes_by_tag(tag_name)
        return JsonResponse(notes, status=status.HTTP_200_OK, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_tags(request, user_id):
    try:
        tags = get_all_tags_from_users_notes(user_id)
        return JsonResponse(tags, status=status.HTTP_200_OK, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user_by_username(request, username):
    try:
        user = get_user(username)
        return JsonResponse(user, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

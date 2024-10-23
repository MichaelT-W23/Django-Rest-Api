from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Permission to only allow access to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

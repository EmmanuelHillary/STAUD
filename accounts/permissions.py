from rest_framework import permissions

class AnonPermission(permissions.BasePermission):
    message = "You are already an authenticated user. Please try to log in."

    def has_permission(self, request, view):
        return not request.user.is_authenticated

from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем своего профиля."""

    def has_object_permission(self, request, view, obj):
        if obj.email == request.user.email:
            return True
        return False


class IsUserActive(permissions.BasePermission):
    """Проверяет, является ли пользователь активным."""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False

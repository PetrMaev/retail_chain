from rest_framework import permissions


class IsFactory(permissions.BasePermission):
    """Проверяет, является ли участник торговой сети заводом."""

    def has_object_permission(self, request, view, obj):
        if int(obj.network_level) == 0:
            return True
        return False

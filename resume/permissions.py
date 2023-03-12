from rest_framework import permissions


class ResumeUpdatePermission(permissions.BasePermission):
    message = 'Редактировать можно только свое резюме'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

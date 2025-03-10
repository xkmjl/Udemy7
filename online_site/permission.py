from rest_framework import permissions


class CheckTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'teacher'


class CheckStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'student'
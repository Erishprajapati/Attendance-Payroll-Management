from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import *
from rest_framework import status
from django.http import response
def get_employee(user):
    """Get Employee profile if exists and user is authenticated"""
    if not user or not user.is_authenticated:
        return None
    return getattr(user, 'Employee_profile', None)

class IsEmployee(BasePermission):
    """Allow access only to users with role = 'EMPLOYEE'"""
    def has_permission(self, request, view):
        emp = get_employee(request.user)
        if not emp:
            return False
        return emp.role == 'EMPLOYEE'

class IsHR(BasePermission):
    """Allow access to HR, ADMIN, or MANAGER roles"""
    def has_permission(self, request, view):
        emp = get_employee(request.user)
        if not emp:
            return False
        return emp.role in ['HR', 'ADMIN', 'MANAGER']
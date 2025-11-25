from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Allows access only to users with specific roles.
    """
    allowed_roles = []  # Override in subclasses

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.roles in self.allowed_roles
        )
    
class IsAdmin(RolePermission):
    allowed_roles = ['admin']


class IsManager(RolePermission):
    allowed_roles = ['manager', 'admin']


class IsVendor(RolePermission):
    allowed_roles = ['vendor', 'admin']


class IsModerator(RolePermission):
    allowed_roles = ['moderator', 'admin']


class IsCustomer(RolePermission):
    allowed_roles = ['customer', 'admin']

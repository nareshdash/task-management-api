from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'admin':
            return True

        # User can only access their own object
        return obj.user == request.user
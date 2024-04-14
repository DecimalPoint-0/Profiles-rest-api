from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users that are logged in to only update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Checks to see if the user has permission to update the object"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
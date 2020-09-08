
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'You must be the author of this object.'


    def has_object_permission(self, request, view, obj):    
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        my_safe_mathod=['PUT','GET']
        if request.method in permissions.SAFE_METHODS:
            return True

        # # Instance must have an attribute named `owner`.
        return obj.author.user==request.user




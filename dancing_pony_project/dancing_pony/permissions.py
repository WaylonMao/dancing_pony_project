from rest_framework.permissions import BasePermission


class CanRateDish(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is Sméagol
        smeagol_username = "Sméagol"
        if request.user.username == smeagol_username:
            return False

        return True

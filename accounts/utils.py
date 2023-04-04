from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


def set_inactive_users():
    from .models import User
    """
    Set inactive status for users who haven't logged in for more than 30 days
    """
    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=thirty_days_ago, is_active=True)
    for user in inactive_users:
        user.is_active = False
        user.save()


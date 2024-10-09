"""
Signals to be triggered for User Functionality.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from user.models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_friend_list(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from user_profile.models import Profile

User = get_user_model()


@receiver(sender=User, signal=post_save)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(sender=User, signal=post_save)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

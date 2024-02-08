from django.db import models
from django.conf import settings
from django.utils.text import slugify
from PIL import Image


def upload_to(instance, filename):
    return 'users/{filename}'.format(filename=filename)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True,)
    county = models.CharField(
        max_length=50, verbose_name="Name of County", null=True)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        # If the slug is not set or empty, generate it using the first and last name
        if not self.slug:
            self.slug = slugify(
                f"{self.user.first_name} {self.user.last_name}")

        super().save(*args, **kwargs)

    def __str__(self):
        if self.user.first_name.endswith("s"):
            return f"{self.user.first_name}' Profile"
        else:
            return f"{self.user.first_name}'s Profile"

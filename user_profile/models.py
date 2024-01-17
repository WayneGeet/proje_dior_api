from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(default="default.jpg", upload_to="users")
    county = models.CharField(
        max_length=50, verbose_name="Name of County", null=True)
    slug = models.SlugField(default="", null=True)

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

from django.contrib.gis.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.text import slugify


class MyUserManager(BaseUserManager):
    def create_user(self, email, id_no, first_name, slug, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            id_no=id_no,
            first_name=first_name,
            last_name=last_name,
            slug=slug
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id_no, first_name, slug, last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            id_no=id_no,
            first_name=first_name,
            last_name=last_name,
            slug=slug
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=20, unique=True,
                             verbose_name="ID number")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["id_no", "first_name", "last_name", "slug"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # If the slug is not set or empty, generate it using the first and last name
        if not self.slug:
            self.slug = slugify(
                f"{self.first_name} {self.last_name}")

        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.auth import get_user_model
# from . import views

User = get_user_model()
# Create your models here.


class YesProjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(approved=True)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Project(gis_models.Model):
    PROJECT_PHASE = (
        ("initial", "initial"),
        ("planning", "planning"),
        ("execution", "execution"),
        ("closing", "closing")
    )
    location = gis_models.PointField()
    name = gis_models.CharField(
        verbose_name="name of the project", max_length=255, unique=True)
    budget = gis_models.CharField(max_length=10)
    start_date = gis_models.DateField(auto_now_add=True)
    photo = gis_models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    phase = gis_models.CharField(verbose_name="project phase",
                                 default="execution", choices=PROJECT_PHASE)
    county = gis_models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name="the county where the project is situated in")
    about = gis_models.TextField(max_length=250, null=True, blank=True, )
    project_type = gis_models.CharField(max_length=50, null=True, blank=True)
    user = gis_models.ForeignKey(
        User, on_delete=gis_models.CASCADE, related_name="projects", null=True)
    # Custom manager class
    # approved = gis_models.BooleanField(default=True, null=True)
    # approved_projects = YesProjects()
    objects = models.Manager()

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse(views.ProjectModelViewSet, kwargs={"pk": self.id})


class Likes(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_likes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_likes")

    comment = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name}"

    class Meta:
        unique_together = ('user', 'project')

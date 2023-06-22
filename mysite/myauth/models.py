from django.contrib.auth.models import User
from django.db import models


def profile_avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"
        ordering = ["id"]

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name="пользователь", related_name="profile")
    fullname = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=11, null=True)
    avatar = models.ImageField(upload_to=profile_avatar_directory_path, null=True, blank=True)

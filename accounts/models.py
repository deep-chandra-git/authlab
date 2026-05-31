from django.db import models


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100,
        blank=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.user.email
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image_profile = models.ImageField(upload_to='images/profile/%Y/%m/',
                                      blank=True, null=True)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return str(self.id)
    
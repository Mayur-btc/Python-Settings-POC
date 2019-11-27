from django.utils.timezone import now
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from accounts.constant import gender_choices
from django.core.validators import MaxLengthValidator,MinLengthValidator

class User(AbstractUser):
    image = models.ImageField(upload_to='images/profile_image/', default='user-default.png')
    phone_number = models.CharField(null=True,max_length=13,validators=[MaxLengthValidator(13),MinLengthValidator(10)])
    gender = models.CharField(choices=gender_choices, null=True, max_length=10)
    birthday = models.DateField(null=True)

    class Meta:
        ordering = ['username', ]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('home')

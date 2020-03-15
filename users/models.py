from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from core.models import data_upload_to as upload_to
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ProcessedImageField(upload_to="avatars", processors=[ResizeToFill(120, 120)], format='JPEG', options={'quality': 60})
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    birthdate = models.DateField(blank=True, null=True)
from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


# Create your models here.
#
#
# class AvailableTime(TimeStampedModel):
#     """
#     Model to save the available times of a user
#     Validations:
#     No user can have overlapping times.
#     """
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='available_time')
#     starttime = models.DateTimeField()
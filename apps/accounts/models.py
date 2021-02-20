from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


# Create your models here.
class User(AbstractUser):
    """
    User model to save the details of both the interview and candidate.
    """
    CANDIDATE = 'candidate'
    INTERVIEWER = 'interviewer'

    USER_TYPES = (
        (CANDIDATE, _('Candidate')),
        (INTERVIEWER, _('Interviewer')),
    )

    user_type = models.CharField(_("User Type"), max_length=125, choices=USER_TYPES, default=INTERVIEWER)

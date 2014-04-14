from django.db import models
from django.db.models import permalink
from django.conf import settings

from django.contrib.auth.models import User



class UserProfile:
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)

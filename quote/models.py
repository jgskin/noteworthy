"""Quote models"""

import re
from django.db import models
from django.core.exceptions import ValidationError

class InvalidUrlSafeNameError(ValidationError):
    """Represents a invalid name for a url"""
    pass

def validate_urlsafe(value):
    """Verify value to be a valid string for a url"""
    if re.search("[^a-z0-9\-]", value):
        raise InvalidUrlSafeNameError("Please insert a valid value."
            " eg:[a-z0-9\-]")

class Group(models.Model):
    """Groups for quote organization"""
    name = models.CharField(max_length=50, unique=True,
        validators=[validate_urlsafe])
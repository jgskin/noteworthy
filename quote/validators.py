"""Validators for the quote app"""

import re
from django.core.exceptions import ValidationError

class InvalidUrlSafeNameError(ValidationError):
    """Represents a invalid name for a url"""
    pass

def validate_urlsafe(value):
    """Verify value to be a valid string for a url"""
    if re.search("[^a-z0-9\-]", value):
        raise InvalidUrlSafeNameError("Please insert a valid value."
            " eg:[a-z0-9\-]")
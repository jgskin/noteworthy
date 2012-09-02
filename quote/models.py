"""Quote models"""

from django.db import models
from quote.validators import validate_urlsafe

class Group(models.Model):
    """Groups for quote organization"""
    name = models.CharField(max_length=50, unique=True,
        validators=[validate_urlsafe])

class Quote(models.Model):
    """The quote entity"""
    text = models.TextField()
    author = models.CharField(max_length=50)
    group = models.ForeignKey(Group, related_name="quotes")
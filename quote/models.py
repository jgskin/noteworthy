"""Quote models"""

from django.db import models
from quote.validators import validate_urlsafe

class Group(models.Model):
    """Groups for quote organization"""
    name = models.CharField(max_length=50, unique=True,
        validators=[validate_urlsafe])

    def __unicode__(self):
        return self.name

class Quote(models.Model):
    """The quote entity"""
    text = models.TextField()
    author = models.CharField(max_length=50)
    group = models.ForeignKey(Group, related_name="quotes")

    def __unicode__(self):
        return "quote {0} from author {1}".format(self.id, self.author)
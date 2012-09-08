"""Quote models"""
# -*- coding: utf-8 -*-

import json
import random
from django.db import models
from quote.validators import validate_urlsafe

class EmptyQuoteSetError(Exception): pass

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

def get_random_quote(group_name):
    """Get a random quote from a group_name"""
    try:
        group = Group.objects.get(name=group_name)
        return random.choice(group.quotes.all())
    except (Group.DoesNotExist, IndexError):
        raise EmptyQuoteSetError, "No quotes found for {0}".format(group_name)

def get_random_quote_json(group_name):
    """Get a random quote in json format for a group name"""
    try:
        quote = get_random_quote(group_name)
        response = {"text": quote.text, "author": quote.author}
    except EmptyQuoteSetError:
        response = {"not_found": True}

    return json.dumps(response)
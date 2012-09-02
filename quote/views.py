"""views for quote app"""

from quote.models import get_random_quote_json
from django.http import HttpResponse

def quote_by_group(request, name):
    """Interface that returns a single quote by a group name"""
    return HttpResponse(get_random_quote_json(name), content_type="application/json")
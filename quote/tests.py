# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

## Tests requirements for group entity: ##
* A group must have an unique and url-safe name

## Tests requirements for quote entity: ##
* A quote must have a text, an author, which defaults to "anonymous", and a group.
"""

import string
from django.test import TestCase
from quote import models as quote_models
from django.core.exceptions import ValidationError
        
good_values = string.lowercase + string.digits + "-"

class GoodInputUrlSafe(TestCase):
    """Tests the validate_urlsafe function of the quote.models module with good input"""

    def test_urlsafe_goodinput(self):
        """Tests the function with all allowed values"""
        quote_models.validate_urlsafe(good_values)

class BadInputValidateUrlSafe(TestCase):
    """Tests the validate_urlsafe function with bad input"""

    #some examples of bad values
    bad_values_sample = (";", ".", "_", "ç", " ", "/", "\\")

    def test_urlsafe_badinput(self):
        """Test the the function with not allowed values"""
        for bad_value in self.bad_values_sample:
            self.assertRaises(quote_models.InvalidUrlSafeNameError,
                quote_models.validate_urlsafe,
                good_values + bad_value)

class ValidGroupCase(TestCase):
    """The valid group test case

    Valid caracteres [a-z\-]*"""
    
    def test_valid_urlsafe_name(self):
        """Test the group validation with a valid name"""
        gr = quote_models.Group()
        gr.name = "a-valid-name"
        gr.clean_fields()

class InvalidGroupCase(TestCase):
    """The invalid group test case"""

    def test_invalid_urlsafe_name(self):
        """Test the group validation with a invalid name"""
        gr = quote_models.Group()
        gr.name = '*invalidcaracterinserted*'
        self.assertRaises(ValidationError, gr.clean_fields)

    def test_duplicated_name(self):
        """Test for a unique name"""
        pass #todo - how to simulate a duplicated name in db?
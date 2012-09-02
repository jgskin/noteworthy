"""Tests for the quote app"""
# -*- coding: utf-8 -*-

import string
from quote import models
from quote import validators
from django.test import TestCase
from django.core.exceptions import ValidationError

# Validators tests
#validate_urlsafe validator test
class ValidateUrlSafeCase(TestCase):
    #all allowed values
    good_values = string.lowercase + string.digits + "-"

class ValidateUrlSafeSuccessCase(ValidateUrlSafeCase):
    """Tests the validate_urlsafe function of the quote.models module with good input"""
    def test_urlsafe_goodinput(self):
        """Tests the function with all allowed values"""
        validators.validate_urlsafe(self.good_values)

class ValidateUrlSafeFailureCase(ValidateUrlSafeCase):
    """Tests the validate_urlsafe function with bad input"""
    #some examples of bad values
    bad_values_sample = (";", ".", "_", "ç", " ", "/", "\\")

    def test_urlsafe_badinput(self):
        """Test the the function with not allowed values"""
        for bad_value in self.bad_values_sample:
            self.assertRaises(validators.InvalidUrlSafeNameError,
                validators.validate_urlsafe,
                self.good_values + bad_value)

#models test
#group entity test
class GroupCase(TestCase):
    """Tests the group entity for success"""
    
    def test_urlsafe_name_validation(self):
        """Test with a url-safe name"""
        gr = models.Group()
        gr.name = "a-valid-name"
        gr.clean_fields()

    def test_add_quote(self):
        """Test with a valid quote

The group can have many quotes,
so we gonna test for the create quote django synthax.
        """
        # save a group is necessary for the quote association
        gr = models.Group(name="a-valid-name")
        gr.save()
        #create a new quote
        gr.quotes.create()

class GroupFailureCase(TestCase):
    """Test the group entity for failure"""

    def test_urlsafe_name_validation(self):
        """Test the group validation with a invalid name"""
        gr = models.Group()
        gr.name = '*invalidcaracterinserted*'
        self.assertRaises(ValidationError, gr.clean_fields)

    def test_duplicated_name(self):
        """Test for a unique name"""
        pass #todo - how to simulate a duplicated name in db?

class QuoteCase(TestCase):
    def setUp(self):
        #save a group for validation success
        agroup = models.Group(name="a-valid-name")
        agroup.save()
        #a valid quote
        self.quote = models.Quote(text="a valid, but short, text.",
            author="Seu madruga", group=agroup)

#quote entity test
class QuoteSuccessCase(QuoteCase):
    """Test the quote entity for success"""
    def test_quote_validation_success(self):
        """Test a quote with text, author and a group"""
        self.quote.full_clean()

class QuoteFailureCase(QuoteCase):
    """Test the quote entity for failure"""
    def test_validation_without_text(self):
        """Test a quote validation without a text"""
        self.quote.text = None
        self.assertRaises(ValidationError, self.quote.full_clean)
    def test_validation_without_author(self):
        """Test a quote validation without a author"""
        self.quote.author = None
        self.assertRaises(ValidationError, self.quote.full_clean)
    def test_validation_without_group(self):
        """Test a quote validation without a group"""
        self.quote.group.delete()
        self.assertRaises(ValidationError, self.quote.full_clean)
#!/usr/bin/python3
""" test for user """
import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class test_User(test_basemodel):
    """ this will test the user class """

    def __init__(self, *args, **kwargs):
        """ initializes the test process """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ checks the first name attributes """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ checks the last name attributes """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ checks the email attributes """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ checks the password attributes """
        new = self.value()
        self.assertEqual(type(new.password), str)

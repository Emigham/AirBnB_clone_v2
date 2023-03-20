#!/usr/bin/python3
""" test for user """
import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class test_User(test_basemodel):
    """ this will test the user class """

     @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

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


if __name__ == "__main__":
    unittest.main()

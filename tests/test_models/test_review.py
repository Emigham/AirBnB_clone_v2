#!/usr/bin/python3
""" test for review """
import unittest
import os
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8


class test_review(test_basemodel):
    """ this will test the review class """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


    def __init__(self, *args, **kwargs):
        """ initializes the tests """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ checks for place attributes """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ checks for user attributes """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ checks for test attributes """
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()

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

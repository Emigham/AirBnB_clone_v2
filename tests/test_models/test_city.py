#!/usr/bin/python3
""" Test for city """
import unittest
import os
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8



class test_City(test_basemodel):
    """ This will test the city class """

    def __init__(self, *args, **kwargs):
        """ test set up and teardown """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing for state attributes"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ checking for name attributes """
        new = self.value()
        self.assertEqual(type(new.name), str)

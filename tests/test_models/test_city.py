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

     @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

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


if __name__ == "__main__":
    unittest.main()

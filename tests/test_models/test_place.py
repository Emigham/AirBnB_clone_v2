#!/usr/bin/python3
""" Test for place """
import unittest
import os
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pep8


class test_Place(test_basemodel):
    """ testing place class """

    def __init__(self, *args, **kwargs):
        """ initialize test process """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ check city attributes """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ check user attributes """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ check for name attributes """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ check for description attributes """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ check for number of rooms attribute """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ checks for number of bathrooms attributes """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ checks the maximum guest attributes """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ checks for price attributes """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ checks location attribute """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ checks location attributes """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ checks amenity attributes """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

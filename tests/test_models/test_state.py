#!/usr/bin/python3
""" test for state """
import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pep8


class test_state(test_basemodel):
    """ this will test the state class """

    def __init__(self, *args, **kwargs):
        """ initializes the test """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ checks the name attributes """
        new = self.value()
        self.assertEqual(type(new.name), str)

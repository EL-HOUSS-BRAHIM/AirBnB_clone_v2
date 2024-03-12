#!/usr/bin/python3
""" document documt """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ document documt """

    def __init__(self, *args, **kwargs):
        """ document documt """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ document documt """
        # Create an instance of City with state_id set to a string
        new = self.value(state_id="some_state_id")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ document documt """
        # Create an instance of City with name set to a string
        new = self.value(name="some_name")
        self.assertEqual(type(new.name), str)


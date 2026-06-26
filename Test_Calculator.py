import unittest
from unittest import TestCase

import Calculator as calc
import Module8 as m8


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, calc.add(2, 3))

    def test_create_person(self):
        # Arrange
        jordan = m8.Person("Jordan", 29, "Trainer")
        # Act
        actual = jordan.speak()
        # Assert
        self.assertEqual("Jordan", jordan.name)
        self.assertEqual(29, jordan.age)
        self.assertEqual("Trainer", jordan.profession)
        self.assertEqual("Jordan says hi!", actual)



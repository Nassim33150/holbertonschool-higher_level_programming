#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base


class TestInstantiationBase(unittest.TestCase):
    def test_instantiation(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)


class TestBaseAttributes(unittest.TestCase):
    def test_id_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_not_none(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_float(self):
        b1 = Base(10.5)
        self.assertEqual(b1.id, 10.5)

    def test_id_negative(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_id_string(self):
        b1 = Base("school")
        self.assertEqual(b1.id, "school")

    def test_id_double_int(self):
        with self.assertRaises(TypeError):
            b1 = Base(10, 10)

    def test_id_double_float(self):
        with self.assertRaises(TypeError):
            b1 = Base(10.5, 10.5)

    def test_id_list(self):
        b1 = Base((10, 5, 2))
        self.assertEqual(b1.id, (10, 5, 2))

    def test_id_dict(self):
        b1 = Base({"id": 1})
        self.assertEqual(b1.id, ({"id": 1}))


if __name__ == '__main__':
    unittest.main()

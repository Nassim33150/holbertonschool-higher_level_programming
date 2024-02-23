#!/usr/bin/python3
""" Module for test Rectangle class """
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
from models.Square import Square

class TestInstantiationSquare(unittest.TestCase):
    def test_instantiation(self):
        s1 = Square()
        self.assertIsInstance(s1, Square)

class TestAttributesSquare(unittest.TestCase):
    def test_id_none(self):
        s1 = Square()
        self.assertEqual(s1.id, 1)

class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5, 10, 3, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)
    
    def test_area(self):
        s1 = Square(5, 5)
        self.assertEqual(s1.area(), 25)
    
    def test_display(self):
        s1 = Square(2, 2)
        expected_output = "##\n" \
                          "##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
    
    def test_str(self):
        s1 = Square(4, 6, 1, 7)
        self.assertEqual(str(r1), "[Square](7) 1/7 - 6/6")
    
    def test_update_args(self):
        s1 = Square(1, 2)
        s1.update(5, 4, 1, 0)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 0)

    def test_update_kwargs(self):
        s1 = Square(1, 2)
        s1.update(id=5, size=10, x=1, y=0)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 0)
    
    def test_dictionnary_representation(self):
        s1 = Square(10, 3, 4, 7)
        self.assertEqual(s1.to_dictionary, {'id': 7, 'size': 10, 'x': 3, 'y': 4})

    
class TestBaseToJSON(unittest.TestCase):
    def test_to_json_string(self):
        s1 = Square(7, 2, 8)
        dictionary = s1.to_dictionary()
        self.assertEqual(Rectangle.to_json_string([dictionary]), '{"size": 7, "x": 2, "y": 8}')


class TestSaveJsonToFile(unittest.TestCase):
    def test_save_to_file(self):
        s1 = Square(10, 2, 8)
        s2 = Square(4)
        self.assertEqual(Rectangle.save_to_file([s1, s2]), [{"y": 8, "x": 2, "id": 1, "size": 10}, {"y": 0, "x": 0, "id": 2, "size": 4}])

#!/usr/bin/python3
""" Module for test Rectangle class """
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestInstantiationRectangle(unittest.TestCase):


class TestAttributesRectangle(unittest.TestCase):
    def test_id_none(self):
        r1 = Rectangle()
        self.assertEqual(r1.id, 1)


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

    def test_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        r1 = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 7)
        self.assertEqual(str(r1), "[Rectangle](7) 2/1 - 4/6")

    def test_update_args(self):
        r1 = Rectangle(1, 2)
        r1.update(5, 3, 4, 1, 0)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)

    def test_update_kwargs(self):
        r1 = Rectangle(1, 2)
        r1.update(id=5, width=3, height=4, x=1, y=0)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)
    
    def test_dictionnary_representation(self):
        r1 = Rectangle(10, 5, 3, 4, 7)
        self.assertEqual(r1.to_dictionary, {'id': 7, 'width': 10, 'height': 5, 'x': 3, 'y': 4})

class TestBaseToJSON(unittest.TestCase):
    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(Base.to_json_string([dictionary]), [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])

    
class TestSaveJsonToFile(unittest.TestCase):
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        self.assertEqual(Base.save_to_file([r1, r2]), [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])

class TestJsonString(unittest.TestCase):
    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
        self.assertEqual(Rectangle.to_json_string(list_input), '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]')    

if __name__ == '__main__':
    unittest.main()

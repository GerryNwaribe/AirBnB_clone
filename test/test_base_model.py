
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_my_number_assignment(self):
        my_model = BaseModel()
        a = 42
        my_model.my_number = a
        self.assertEqual(my_model.my_number, a)

    def test_name_assignment(self):
        my_model = BaseModel()
        my_model.name = ""
        self.assertEqual(my_model.name, "")

    def test_empty_string_assignment(self):
        my_model = BaseModel()
        my_model.my_number = ""
        self.assertEqual(my_model.my_number, "")

    def test_none_assignment(self):
        my_model = BaseModel()
        my_model.name = None
        self.assertIsNone(my_model.name)
    
    def no_attribute(self):
        my_model = BaseModel()
        my_model.my_number
        self.assertEqual(my_model.my_number)

    def test_model_operations(self):
        my_model = BaseModel()
        my_model.name = "name"
        
        self.assertIsNone(my_model.my_number)  
        expected_str = f"[BaseModel] ({my_model.id}) {{'name': 'name', 'my_number': None, 'created_at': '{my_model.created_at.isoformat()}', 'updated_at': '{my_model.updated_at.isoformat()}'}}"
        self.assertEqual(str(my_model), expected_str)

        my_model.save()

        expected_updated_str = f"[BaseModel] ({my_model.id}) {{'name': 'name', 'my_number': None, 'created_at': '{my_model.created_at.isoformat()}', 'updated_at': '{my_model.updated_at.isoformat()}'}}"
        self.assertEqual(str(my_model), expected_updated_str)
        
        my_model_dict = my_model.to_dict()
        expected_dict = {
            'id': my_model.id,
            'name': 'name',
            'my_number': None,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(my_model_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
<<<<<<< HEAD
my_model.name = "name"
my_model.my_number
=======
my_model.name = "My First Model"
my_model.my_number = 89
>>>>>>> 035fd5af54c8782ed23d287e1ad12b93547ca0b8
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
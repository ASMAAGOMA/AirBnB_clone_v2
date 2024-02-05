#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the list of objects of one type of class.
        If cls is None, returns all objects.
        """
        if cls is None:
            return self.__objects.values()
        else:
            return [obj for obj in self.__objects.values() if isinstance(obj, cls)]
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                data = json.load(json_file)
                for key, val in data.items():
                    class_name = val.pop('__class__', None)
                    if class_name in classes:
                        self.all()[key] = classes[class_name](**val)
                    else:
                        print(f"Unknown class: {class_name}")
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj == None:
            return
        the_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if the_key in self.__objects.keys():
            del self.__objects[the_key]

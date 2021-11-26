#!/usr/bin/python3

class file_storage:
    """
    Stores Python Dictionaries as a Jason File
    """
    __file_path = "file.json"
    __objects = {}

@classmethod
def all(self):
    """
    Returning the dictionary
    """
    return(self.__objects)

def new(self,obj):
    """
    To insert an object into the object dictionary
    """
    self.__objects.update({"{}.{}".format(obj.__class__.__name__, obj.id: obj)})

def save(self):
    """
    Serializes Objects to Json File. I.E to Insert the object into the Json File.
    """
    with open(self.__file_path, mode="w") as f:
        for key, value in self.__objects.items():
            d1[key] = value.to.dict()
            json.dump(d1, f)

def reload(self):
            """
        Reload will deserialize a JSON formatted file to an __object
        *** Only if it exists!
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                readit = json.load(f)
                for value in readit.values():
                    a = eval("{}(**value)".format(value["__class__"]))
                    self.new(a)
    
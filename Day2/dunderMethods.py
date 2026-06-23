#Dunder methods

class AIModel:
    #__init__ runs after the object is created and is used to initialized the instance
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version
#__str__ is the nice printable version used by print() and str()
    def __str__(self):
        return f"Model: {self.model_name} | version {self.version}"
    
#__repr__ is the "official" representation and is meant to be debugging-friendly
    def __repr__(self):
        return f"AIModel(model_name = {self.model_name}, version = {self.version})"

model = AIModel("Linear Regression", "1.0")
repr(model)
print(model)

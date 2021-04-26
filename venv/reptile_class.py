# Reptile class

# Importing the Animal class
from OOP import Animal


# inheriting the animal class
class Reptile(Animal):

    # initialise the reptile class
    def __init__(self):
        super().__init__()  # initialising everything from the parent class
        self.cold_blooded = True

    def use_venom(self):
        print("If i have venom, I am going to use it")

    def moving(self):
        print("moving but as a snake")

    # representation of a class
    def __repr__(self):
        return f"This is a reptile"

    # str will change the output for when the object is printed directly
    def __str__(self):
        return f"string version of this reptile"


bob = Reptile()
print(repr(bob))

# Print the name of the file
print(__name__)  # name of the file is OOP as we are importing the library in which the class is inherited

# Different programming paradigms

# Python: Functional, imperative, OOP, procedural

# SQL: declarative

'''
4 pillars of OOP : Abstraction, Encapsulation, Inheritance, Polymorphism

Abstraction: hiding the internal details of how things work (whenever we are writing a function or classes, we are using abstractions). The user is kept unaware of the inner workings of the method

Encapsulation: hiding things and making them inaccessible (the use of underscores __current_speed)

Inheritance: Where the child class can inherit the attributes of the parent class

Polymorphism: poly means many, morphism means form. Create a structure that takes many forms. Can have methods of the same name that take different forms
'''


# Animal class
class Animal:
    # initialisation
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    # Methods   # All of the methods are abstracted away
    def breath(self):
        print("one breath in and one out")

    def eat(self):
        print("nom nom nom")

    def moving(self):
        print("forwards, backwards and side to side")


# Breathing has been abstracted, because the user doesnt know how the cat can breath
cat = Animal()
cat.breath()

# Print the name of this file
print(__name__)  # name of the file is __main__, it means that we are running it directly

# If we want to inherit the functionality of the class but differentiating between the 2 files
# We would use this only if we want to run code for a specific file esp if the file we are
# running is going to be imported into other files
if __name__ == '__main__':
    cat = Animal()
    cat.breath()
    print(__name__)

# Class representation: function to represent classes

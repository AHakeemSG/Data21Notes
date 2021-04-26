# Naming conventions for classes, use CamelCase
class Dog:
    animal_kind = "canine"

    def bark(self):  # Method - this method is referring to he class of Dog
        return "woof"


# Example class
class AmazingDog:
    animal_kind = "canine"

    def bark(self):
        print(self.animal_kind)  # If we create a class, we have to reference self before the variable
        return "woof"


Bob = AmazingDog()
Sue = AmazingDog()
Bob.animal_kind = "dolphin"
print(bob.animal_kind)


# Example class initialisation
class AmazingDog:

    def __init__(self, animal_kind):  # initialisation: making an instance of class upon creation
        self.animal_kind = "canine"
        self.bark()  # calling in class methods into the initialization method
        #  _is_alive = True  # One _ hides the is_alive
        # __is_alive = True  # Two __ doesnt allow us to access the is_alive

    def bark(self):
        print(self.animal_kind)
        return "woof"

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status  # allows people to access and change things within the method, not outside it


Bob = AmazingDog("canine")
Sue = AmazingDog("dolphin")
print(Bob.animal_kind)
print(Sue.animal_kind)
print(Bob.get__is_alive())
# Bob.__is_alive = False


# Exercise: Create a car class
'''
Create a car class. Give the vehicle a maximum speed, 
and keep track of the current speed of the vehicle. 
It doesn't make sense for the speed to be adjusted directly, 
so put an underscore in front of it and implement a speed getter 
as well as accelerate and brake setter methods that change the speed in a logical way.
Do your methods make sense? Does braking past 0 cause the speed to increase? Can you accelerate past the car's top speed?

Components of the class: 
max speed, 
current speed, 
method that would accelerate (cap the speed) 
method that will break (make sure it doesnt go below 0)
'''


# Creating a class: Car
class Car:

    # Initialising the class  - self should always be the first parameter in a class
    def __init__(self, manufacturer, model, engine_size, num_of_cylinders, car_year, num_of_wheels,
                 max_speed, colour, number_of_doors, num_of_windows, current_speed):
        self.manufacturer = manufacturer
        self.model = model
        self.engine_size = engine_size
        self.num_of_cylinders = num_of_cylinders
        self.car_year = car_year
        self.num_of_wheels = num_of_wheels
        self.max_speed = max_speed
        self.colour = colour
        self.num_of_doors = number_of_doors
        self.num_of_windows = num_of_windows
        self.current_speed = current_speed

    # Method of car details through class representation
    def __repr__(self):  # repr is the representation function
        car_details = f"Manufacturer: {self.manufacturer + ',': <20} Model: {self.model + ',': <15} " \
                      f"Engine Size: {self.engine_size + ',': <15} Number of Cylinders: {self.num_of_cylinders + ',': <10}" \
                      f"Car Year: {self.car_year + ',': <10} Number of Wheels: {self.num_of_wheels + ',': <10}" \
                      f"Max Speed: {self.max_speed + ',': <15} Colour of Car: {self.colour + ',': <10}" \
                      f"Number of Doors: {self.num_of_doors + ',': <10} Number of Windows: {self.num_of_windows + ',': <10}" \
                      f"Current Speed: {self.current_speed + ',': <15}"
        return car_details

    # Method of the changing of speed
    def speed_change(self, amount: int):
        new_speed = self.__current_speed + amount
        if new_speed >= self.max_speed:
            self.__current_speed = self.max_speed
        elif new_speed <= 0:
            self.__current_speed = 0
        else:
            self.current_speed = new_speed


# Cars data
mercedes_benz = Car("Mercedes Benz", "C63", "4.0-liter V8", 4, 2021, 4, 155, "Black", 2, 4, 0)
ferrari = Car("Ferrari", "Enzo", "6.0-liter V12", 12, 2002, 4, 218, "Red", 2, 2)
toyota = Car("Toyota", "Auris", "1.6", 4, 2016, 4, 110, "White", 4, 4)

mercedes_benz.speed_change(int(input("How much do you want to change your speed by? ")))


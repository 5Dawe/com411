
class Robot:
    # define a class attribute
    MAX_ENERGY = 100

    def __init__(self):
        #set instance attributes
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    # a method grow that increases the age of the object by 1
    def grow(self):
        self.age = self.age + 1
        return

    # a method eat that takes an amount as a parameter.
    # This should increase the energy of the object by the amount.
    # Note, energy should not exceed MAX_ENERGY.
    def eat(self, amount):
        for count in amount:
            if self.energy < Robot.MAX_ENERGY:
                self.energy = self.energy + 1
            else:
                pass
        return

    # a method move that takes a distance as a parameter.
    # This should reduce the energy of the object by the distance.
    # Note, energy should not fall below 0.
    def move(self, distance):
        for step in distance:
            if self.energy > 0:
                self.energy = self.energy - 1
            else:
                pass
        return

    def display(self):
        print(f"I am {self.name}")

#The function repr returns a formal string representation of the object
    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

#the function str returns an informal string representation of the object.
    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'


if (__name__ == "__main__"):
    Robot = Robot()
    Robot.display()
    #print str
    print(Robot)
    #print repr
    print(repr(Robot))

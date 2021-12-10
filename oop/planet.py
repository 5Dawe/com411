from human import Human
from robot import Robot


class Planet:
    def __init__(self):
        #set instance attributes
        self.humans = []
        self.robots = []

    #set instance methods
    def add_human(self, added_human):
        self.humans.append(added_human)
        return

    def remove_human(self, removed_human):
        self.humans.remove(removed_human)
        return

    def add_robot(self, added_robot):
        self.robots.append(added_robot)
        return

    def remove_robot(self, removed_robot):
        self.robots.remove(removed_robot)
        return

    # The function repr returns a formal string representation of the object
    def __repr__(self):
        return f"The plants have {self.humans}"

    # the function str returns an informal string representation of the object.
    def __str__(self):
    #    return f"Robot {self.name} is {self.age} years old."


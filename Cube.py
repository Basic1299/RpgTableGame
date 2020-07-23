import random

# class Cube what generates numbers for attack and defense of characters
class Cube(object):
    def __init__(self, sidesNumber=6):
        self.sidesNumber = sidesNumber

    def info(self):
        print(f"The cube with {self.sidesNumber} sides")

    # Generate random number from 1 to sides of cube
    def throw(self):
        return random.randint(1, self.sidesNumber)
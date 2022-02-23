import random 

class Insect:
    def __init__(self,wings,legs,flight):
        self.wings = 4
        self.legs = 3
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_fly(self):
        return self.flight_length

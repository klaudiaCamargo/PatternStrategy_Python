from app.fly.fly_behavior import FlyBehavior
from app.swim.swim_behavior import SwimBehavior

class Duck:
    def __init__(self, name : str, fly_behavior : FlyBehavior, swim_behavior: SwimBehavior):
        self._name = name  # um _ serve para encapsular
        self._fly_behavior = fly_behavior
        self._swim_behavior = swim_behavior

    def get_name(self):
        return self._name

    def quack(self):
        print ("Quack")
        
    def display(self):
        print("O pato: "  + self._name) 

    def fly_behavior(self):
        self._fly_behavior.fly()
    
    def swim_behavior(self):
        self._swim_behavior.swim()
        
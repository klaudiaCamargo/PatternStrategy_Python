from app.duck.abstract_duck import Duck
from app.fly.fly_with_rocket import FlyWithRocket
from app.swim.swim_with_board import SwimWithBoard

class RubberDuck(Duck):
    def __init__ (self, name):
        #solicita o nome e o metodo que esse pato voa
        super().__init__(name, FlyWithRocket(), SwimWithBoard())
    
    
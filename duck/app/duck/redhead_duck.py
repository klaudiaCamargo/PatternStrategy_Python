from app.duck.abstract_duck import Duck
from app.fly.fly_noway import FlyNoway
from app.swim.swim_with_jetski import SwimWithJetski

class RedheadDuck(Duck):
    def __init__(self, name):
        super().__init__(name, FlyNoway(), SwimWithJetski())
    
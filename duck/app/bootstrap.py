from app.duck.mallard_duck import MallardDuck
from app.duck.redhead_duck import RedheadDuck
from app.duck.rubber_duck import RubberDuck

class Startup:
    def execute(self): #self imprime o endereço de memória
        ducks = [
            MallardDuck("Pato Raivoso - Mallard "),
            RedheadDuck("Pato cabeça vermelha - Redhead"),
            RubberDuck("Pato de borracha - Rubber")
        ]
        for duck in ducks:
            print("----------")
            duck.display()
            duck.quack()
            duck.fly_behavior()
            duck.swim_behavior()
     
        
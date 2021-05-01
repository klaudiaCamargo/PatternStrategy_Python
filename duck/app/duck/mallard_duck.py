from app.duck.abstract_duck import Duck
from app.fly.fly_with_wings import FlyWithWings
from app.swim.swim_with_board import SwimWithBoard

class MallardDuck(Duck):
    def __init__ (self, name):
        super().__init__(name, FlyWithWings(), SwimWithBoard()) #solicita o nome e o metodo que esse pato voa

    def swim(self):   #polimorfismo: subescrever um método com comando diferente do metodo ja existente.
        print("Eu não quero nadar")   #não pode mudar a caracteristica total do metodo.
                                #trocar comportamento y por comportamento x, mantendo a mesma assinatura(nome).

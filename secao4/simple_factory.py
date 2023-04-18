from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print('AU au')

class Gato(Animal):

    def falar(self):
        print('Miau')

#Factory
class Fabrica:

    def criar_animal_falante(self, tipo):
        return eval(tipo)().falar()

#Client
if __name__ == '__main__':
    fab = Fabrica()
    animal = input('Qual animal vc deseja?')
    fab.criar_animal_falante(animal)
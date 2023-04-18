from abc import ABCMeta, abstractmethod


# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass


# Concreto Factory A
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()
    
    def criar_pizza(self):
        return PizzaCamarao()

# Concreto Factory B
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocoli()
    
    def criar_pizza(self):
        return PizzaBologna()

# Abstract Produto A
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass

# Abstract Produto B
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass


# Produto Concreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# Produto Concreto
class PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida na com camarão na {type(PizzaVeg).__name__}')


# Produto Concreto
class PizzaBrocoli(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# Produto Concreto
class PizzaBologna(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com bologna na {type(PizzaVeg).__name__}')


# Cliente
class Pizzaria:

    def fazer_pizza(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)

pizzaria = Pizzaria()
pizzaria.fazer_pizza()
# FactoryMethod Pattern

from abc import ABC, abstractmethod


# Product - Interface for Pizza objects
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


# ConcreteProduct - Implements the Pizza interface for Veg Pizzas
class VegPizza(Pizza):
    def prepare(self):
        return "Preparing Veg Pizza"

    def bake(self):
        return "Baking Veg Pizza"

    def cut(self):
        return "Cutting Veg Pizza"

    def box(self):
        return "Packaging Veg Pizza"


# ConcreteProduct - Implements the Pizza interface for Non-Veg Pizzas
class NonVegPizza(Pizza):
    def prepare(self):
        return "Preparing Non-Veg Pizza"

    def bake(self):
        return "Baking Non-Veg Pizza"

    def cut(self):
        return "Cutting Non-Veg Pizza"

    def box(self):
        return "Packaging Non-Veg Pizza"


# Creator - Abstract class for creating Pizzas
class PizzaShop(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


# ConcreteCreator - Implements the factory method to create specific types of Pizzas
class PizzaFactory(PizzaShop):
    def create_pizza(self, pizza_type):
        if pizza_type == "Veg":
            return VegPizza()
        elif pizza_type == "Non-Veg":
            return NonVegPizza()
        else:
            raise ValueError("Invalid pizza type")


# Client Code
if __name__ == "__main__":
    pizza_factory = PizzaFactory()

    veg_pizza = pizza_factory.order_pizza("Veg")
    print(veg_pizza.prepare())
    print(veg_pizza.bake())
    print(veg_pizza.cut())
    print(veg_pizza.box())

    print("\n")

    non_veg_pizza = pizza_factory.order_pizza("Non-Veg")
    print(non_veg_pizza.prepare())
    print(non_veg_pizza.bake())
    print(non_veg_pizza.cut())
    print(non_veg_pizza.box())

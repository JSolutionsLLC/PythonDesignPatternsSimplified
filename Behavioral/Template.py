# Template Pattern

from abc import ABC, abstractmethod


# AbstractClass - Represents the base class for coffee brewing
class CoffeeBrewing(ABC):
    def prepare_coffee(self):
        self.boil_water()
        self.brew_coffee()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew_coffee(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring coffee into cup")


# ConcreteClass - Represents black coffee
class BlackCoffee(CoffeeBrewing):
    def brew_coffee(self):
        print("Brewing black coffee")

    def add_condiments(self):
        print("Adding sugar to black coffee")


# ConcreteClass - Represents latte
class Latte(CoffeeBrewing):
    def brew_coffee(self):
        print("Brewing espresso for latte")

    def add_condiments(self):
        print("Steaming milk and adding to latte")


# Client Code
if __name__ == "__main__":
    print("Making Black Coffee:")
    black_coffee = BlackCoffee()
    black_coffee.prepare_coffee()
    print()

    print("Making Latte:")
    latte = Latte()
    latte.prepare_coffee()

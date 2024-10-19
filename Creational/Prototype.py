# Prototype Pattern

from copy import deepcopy


# Prototype - Interface for cloning animals
class Animal:
    def clone(self):
        pass


# ConcretePrototype - Implements the Animal interface for Lions
class Lion(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"{self.name} (Lion) - {self.age} years old"


# ConcretePrototype - Implements the Animal interface for Sheep
class Sheep(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"{self.name} (Sheep) - {self.age} years old"


# Client Code
if __name__ == "__main__":
    lion_prototype = Lion("Leo", 5)
    sheep_prototype = Sheep("Shaun", 2)

    # Cloning animals
    lion1 = lion_prototype.clone()
    lion2 = lion_prototype.clone()
    lion2.name = "Simba"  # Modifying the cloned lion's name

    sheep1 = sheep_prototype.clone()
    sheep2 = sheep_prototype.clone()
    sheep2.name = "Dolly"  # Modifying the cloned sheep's name

    # Output
    print("Original Lion Prototype:", lion_prototype)
    print("Cloned Lion 1:", lion1)
    print("Cloned Lion 2:", lion2)

    print("\nOriginal Sheep Prototype:", sheep_prototype)
    print("Cloned Sheep 1:", sheep1)
    print("Cloned Sheep 2:", sheep2)

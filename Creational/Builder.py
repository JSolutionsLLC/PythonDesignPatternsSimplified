# Builder Pattern

from abc import ABC, abstractmethod


# Product - Represents the complex object (CustomMeal) that we are building
class CustomMeal:
    def __init__(self):
        self.burger = None
        self.drink = None
        self.side_dish = None

    def __str__(self):
        return f"Burger: {self.burger}, Drink: {self.drink}, Side Dish: {self.side_dish}"


# Builder - Abstract interface for building a custom meal
class MealBuilder(ABC):
    @abstractmethod
    def build_burger(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass

    @abstractmethod
    def get_meal(self):
        pass


# ConcreteBuilder - Implements the Builder interface to construct a specific custom meal
class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = CustomMeal()

    def build_burger(self):
        self.meal.burger = "Veg Burger"

    def build_drink(self):
        self.meal.drink = "Coke"

    def build_side_dish(self):
        self.meal.side_dish = "French Fries"

    def get_meal(self):
        return self.meal


class NonVegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = CustomMeal()

    def build_burger(self):
        self.meal.burger = "Chicken Burger"

    def build_drink(self):
        self.meal.drink = "Pepsi"

    def build_side_dish(self):
        self.meal.side_dish = "Onion Rings"

    def get_meal(self):
        return self.meal


# Director - Controls the construction process of the custom meal
class MealDirector:
    def construct_meal(self, builder):
        builder.build_burger()
        builder.build_drink()
        builder.build_side_dish()
        return builder.get_meal()


# Client Code
if __name__ == "__main__":
    veg_builder = VegMealBuilder()
    non_veg_builder = NonVegMealBuilder()

    director = MealDirector()

    veg_meal = director.construct_meal(veg_builder)
    non_veg_meal = director.construct_meal(non_veg_builder)

    print("Veg Meal:", veg_meal)
    print("Non-Veg Meal:", non_veg_meal)

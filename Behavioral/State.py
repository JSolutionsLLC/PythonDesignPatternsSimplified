# State Pattern

from abc import ABC, abstractmethod


# State - Interface for traffic light states
class TrafficLightState(ABC):
    @abstractmethod
    def change_state(self, traffic_light):
        pass

    @abstractmethod
    def get_color(self):
        pass


# ConcreteState - Represents the Red state of the traffic light
class RedState(TrafficLightState):
    def change_state(self, traffic_light):
        traffic_light.set_state(GreenState())

    def get_color(self):
        return "Red"


# ConcreteState - Represents the Green state of the traffic light
class GreenState(TrafficLightState):
    def change_state(self, traffic_light):
        traffic_light.set_state(YellowState())

    def get_color(self):
        return "Green"


# ConcreteState - Represents the Yellow state of the traffic light
class YellowState(TrafficLightState):
    def change_state(self, traffic_light):
        traffic_light.set_state(RedState())

    def get_color(self):
        return "Yellow"


# Context - Represents the traffic light
class TrafficLight:
    def __init__(self):
        self._state = RedState()

    def set_state(self, state):
        self._state = state

    def change_state(self):
        self._state.change_state(self)

    def get_color(self):
        return self._state.get_color()


# Client Code
if __name__ == "__main__":
    my_traffic_light = TrafficLight()

    print("Current Color:", my_traffic_light.get_color())  # Output: Current Color: Red

    my_traffic_light.change_state()
    # Output: Current Color: Green
    print("Current Color:", my_traffic_light.get_color())

    my_traffic_light.change_state()
    # Output: Current Color: Yellow
    print("Current Color:", my_traffic_light.get_color())

    my_traffic_light.change_state()
    # Output: Current Color: Red
    print("Current Color:", my_traffic_light.get_color())

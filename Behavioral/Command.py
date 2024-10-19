# Command Pattern

from abc import ABC, abstractmethod


# Command - Interface for executing commands
class Command(ABC):
    @abstractmethod
    def execute(self):
        ...


# ConcreteCommand - Represents a command to turn on the TV
class TurnOnTVCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.turn_on()


# ConcreteCommand - Represents a command to turn off the TV
class TurnOffTVCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.turn_off()


# Receiver - Represents the TV that performs the actual actions
class TV:
    def turn_on(self):
        print("TV is turned on")

    def turn_off(self):
        print("TV is turned off")


# Invoker - Represents the remote control
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()


# Client Code
if __name__ == "__main__":
    my_tv = TV()

    turn_on_command = TurnOnTVCommand(my_tv)
    turn_off_command = TurnOffTVCommand(my_tv)

    remote_control = RemoteControl()

    remote_control.set_command(turn_on_command)
    remote_control.press_button()  # Output: TV is turned on

    remote_control.set_command(turn_off_command)
    remote_control.press_button()  # Output: TV is turned off

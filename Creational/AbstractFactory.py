# AbstractFactory Pattern - Interface for creating UI elements

from abc import ABC, abstractmethod


# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# ConcreteFactory for Windows - Implements UIFactory to create Windows UI elements
class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# ConcreteFactory for macOS - Implements UIFactory to create macOS UI elements
class MacOSUIFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


# AbstractProduct - Interface for UI elements
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


# ConcreteProduct for Windows - Implements Button interface for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendered a Windows-style button."


# ConcreteProduct for macOS - Implements Button interface for macOS
class MacOSButton(Button):
    def render(self):
        return "Rendered a macOS-style button."


# ConcreteProduct for Windows - Implements Checkbox interface for Windows
class WindowsCheckbox(Button):
    def render(self):
        return "Rendered a Windows-style checkbox."


# ConcreteProduct for macOS - Implements Checkbox interface for macOS
class MacOSCheckbox(Button):
    def render(self):
        return "Rendered a macOS-style checkbox."


# Client Code
def create_ui(ui_factory):
    button = ui_factory.create_button()
    checkbox = ui_factory.create_checkbox()

    print("Rendering UI elements:")
    print(button.render())
    print(checkbox.render())


if __name__ == "__main__":
    windows_factory = WindowsUIFactory()
    macos_factory = MacOSUIFactory()

    print("Creating UI for Windows:")
    create_ui(windows_factory)

    print("\nCreating UI for macOS:")
    create_ui(macos_factory)

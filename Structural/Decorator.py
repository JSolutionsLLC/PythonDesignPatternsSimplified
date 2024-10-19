# Decorator Pattern

# Component - Interface for text display
class TextDisplay:
    def get_text(self):
        pass


# ConcreteComponent - Represents the basic text display
class BasicTextDisplay(TextDisplay):
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text


# Decorator - Interface for text decorators
class TextDecorator(TextDisplay):
    def __init__(self, text_display):
        self._text_display = text_display

    def get_text(self):
        return self._text_display.get_text()


# ConcreteDecorator - Adds bold functionality
class BoldTextDecorator(TextDecorator):
    def get_text(self):
        return f"<b>{self._text_display.get_text()}</b>"


# ConcreteDecorator - Adds italic functionality
class ItalicTextDecorator(TextDecorator):
    def get_text(self):
        return f"<i>{self._text_display.get_text()}</i>"


# ConcreteDecorator - Adds underline functionality
class UnderlineTextDecorator(TextDecorator):
    def get_text(self):
        return f"<u>{self._text_display.get_text()}</u>"


# Client Code
if __name__ == "__main__":
    basic_text = BasicTextDisplay("Hello, World!")

    bold_text = BoldTextDecorator(basic_text)
    italic_text = ItalicTextDecorator(bold_text)
    underlined_italic_text = UnderlineTextDecorator(italic_text)

    print("Basic Text:", basic_text.get_text())
    print("Decorated Text (Bold, Italic, Underline):", underlined_italic_text.get_text())

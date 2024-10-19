# Flyweight Pattern

# Flyweight - Interface for text formatting options
class TextFormatting:
    def apply_formatting(self, text):
        pass


# ConcreteFlyweight - Represents shared text formatting options
class ConcreteTextFormatting(TextFormatting):
    def __init__(self, font_size, font_color, bold=False, italic=False):
        self._font_size = font_size
        self._font_color = font_color
        self._bold = bold
        self._italic = italic

    def apply_formatting(self, text):
        formatted_text = f"<span style='font-size:{self._font_size}; color:{self._font_color};"
        if self._bold:
            formatted_text += " font-weight:bold;"
        if self._italic:
            formatted_text += " font-style:italic;"
        formatted_text += f"'>{text}</span>"
        return formatted_text


# FlyweightFactory - Manages and caches the TextFormatting objects
class TextFormattingFactory:
    _text_formatting_cache = {}

    @classmethod
    def get_text_formatting(cls, font_size, font_color, bold=False, italic=False):
        key = (font_size, font_color, bold, italic)
        if key not in cls._text_formatting_cache:
            cls._text_formatting_cache[key] = ConcreteTextFormatting(font_size, font_color, bold, italic)
        return cls._text_formatting_cache[key]


# Client Code
if __name__ == "__main__":
    text_formatting1 = TextFormattingFactory.get_text_formatting("12px", "red", bold=True)
    text1 = text_formatting1.apply_formatting("Hello, World!")

    text_formatting2 = TextFormattingFactory.get_text_formatting("12px", "red", bold=True)
    text2 = text_formatting2.apply_formatting("Welcome to the Flyweight Pattern!")

    print("Text 1:", text1)
    print("Text 2:", text2)

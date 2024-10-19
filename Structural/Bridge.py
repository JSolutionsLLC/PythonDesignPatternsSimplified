# Bridge Pattern

# Abstraction - Interface for drawing shapes
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass


# Refinement of Abstraction - Extends Shape to add additional features
class CircleShape(Shape):
    def draw(self):
        return f"Drawing a circle using {self.renderer.render_circle()}"


# Refinement of Abstraction - Extends Shape to add additional features
class SquareShape(Shape):
    def draw(self):
        return f"Drawing a square using {self.renderer.render_square()}"


# Implementation - Interface for rendering shapes
class Renderer:
    def render_circle(self):
        pass

    def render_square(self):
        pass


# ConcreteImplementation - Implements the Renderer interface for SVG
class SvgRenderer(Renderer):
    def render_circle(self):
        return "SVG Circle"

    def render_square(self):
        return "SVG Square"


# ConcreteImplementation - Implements the Renderer interface for PNG
class PngRenderer(Renderer):
    def render_circle(self):
        return "PNG Circle"

    def render_square(self):
        return "PNG Square"


# Client Code
if __name__ == "__main__":
    svg_renderer = SvgRenderer()
    png_renderer = PngRenderer()

    circle = CircleShape(svg_renderer)
    square = SquareShape(png_renderer)

    print(circle.draw())  # Output: Drawing a circle using SVG Circle
    print(square.draw())  # Output: Drawing a square using PNG Square

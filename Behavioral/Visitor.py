# Visitor Pattern

from abc import ABC, abstractmethod


# Visitor - Interface for document visitors
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_paragraph(self, paragraph):
        pass

    @abstractmethod
    def visit_heading(self, heading):
        pass


# ConcreteVisitor - Visitor to count document elements
class CountVisitor(DocumentVisitor):
    def __init__(self):
        self._paragraph_count = 0
        self._heading_count = 0

    def visit_paragraph(self, paragraph):
        self._paragraph_count += 1

    def visit_heading(self, heading):
        self._heading_count += 1

    def get_paragraph_count(self):
        return self._paragraph_count

    def get_heading_count(self):
        return self._heading_count


# ConcreteVisitor - Visitor to convert document elements to HTML
class HTMLVisitor(DocumentVisitor):
    def __init__(self):
        self._html_output = ""

    def visit_paragraph(self, paragraph):
        self._html_output += f"<p>{paragraph.get_text()}</p>"

    def visit_heading(self, heading):
        self._html_output += f"<h{heading.get_level()}>{heading.get_text()}</h{heading.get_level()}>"

    def get_html_output(self):
        return self._html_output


# Element - Interface for document elements
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# ConcreteElement - Represents a paragraph in the document
class Paragraph(DocumentElement):
    def __init__(self, text):
        self._text = text

    def accept(self, visitor):
        visitor.visit_paragraph(self)

    def get_text(self):
        return self._text


# ConcreteElement - Represents a heading in the document
class Heading(DocumentElement):
    def __init__(self, text, level):
        self._text = text
        self._level = level

    def accept(self, visitor):
        visitor.visit_heading(self)

    def get_text(self):
        return self._text

    def get_level(self):
        return self._level


# ObjectStructure - Represents the document with a collection of elements
class Document:
    def __init__(self):
        self._elements = []

    def add_element(self, element):
        self._elements.append(element)

    def remove_element(self, element):
        self._elements.remove(element)

    def accept(self, visitor):
        for element in self._elements:
            element.accept(visitor)


# Client Code
if __name__ == "__main__":
    document = Document()
    document.add_element(Heading("Main Title", 1))
    document.add_element(Paragraph("This is the first paragraph."))
    document.add_element(Heading("Subheading", 2))
    document.add_element(Paragraph("This is the second paragraph."))

    count_visitor = CountVisitor()
    document.accept(count_visitor)
    print("Paragraph Count:", count_visitor.get_paragraph_count())  # Output: Paragraph Count: 2
    print("Heading Count:", count_visitor.get_heading_count())      # Output: Heading Count: 2

    html_visitor = HTMLVisitor()
    document.accept(html_visitor)
    print("HTML Output:\n", html_visitor.get_html_output())
    # Output: HTML Output:
    # <h1>Main Title</h1><p>This is the first paragraph.</p><h2>Subheading</h2><p>This is the second paragraph.</p>

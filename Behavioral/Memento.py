# Memento Pattern


# Memento - Represents the object that stores the internal state of the Originator
class TextEditorMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


# Originator - Represents the object for which the state is to be saved or restored
class TextEditor:
    def __init__(self):
        self._content = ""

    def get_content(self):
        return self._content

    def add_text(self, text):
        self._content += text

    def save_to_memento(self):
        return TextEditorMemento(self._content)

    def restore_from_memento(self, memento):
        self._content = memento.get_content()


# Caretaker - Manages and keeps track of the Mementos
class TextEditorHistory:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        if len(self._history) > 1:
            self._history.pop()
            return self._history[-1]
        else:
            return self._history[0]


# Client Code
if __name__ == "__main__":
    text_editor = TextEditor()
    history = TextEditorHistory()

    text_editor.add_text("Hello, ")
    history.save(text_editor.save_to_memento())

    text_editor.add_text("world!")
    history.save(text_editor.save_to_memento())

    print("Current Content:", text_editor.get_content())  # Output: Current Content: Hello, world!

    text_editor.restore_from_memento(history.undo())
    print("After Undo:", text_editor.get_content())  # Output: After Undo: Hello,

    text_editor.restore_from_memento(history.undo())
    print("After Undo Again:", text_editor.get_content())  # Output: After Undo Again:

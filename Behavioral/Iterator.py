# Iterator Pattern

from abc import ABC, abstractmethod


# Iterator - Interface for traversing the collection
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# ConcreteIterator - Provides the implementation for traversing a list
class ListIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration


# Aggregate - Interface for creating an Iterator
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


# ConcreteAggregate - Implements the Aggregate interface to create a ConcreteIterator
class NumberList(Aggregate):
    def __init__(self):
        self._numbers = []

    def add_number(self, number):
        self._numbers.append(number)

    def create_iterator(self):
        return ListIterator(self._numbers)


# Client Code
if __name__ == "__main__":
    number_list = NumberList()
    number_list.add_number(1)
    number_list.add_number(2)
    number_list.add_number(3)

    iterator = number_list.create_iterator()

    while iterator.has_next():
        print(iterator.next())  # Output: 1\n2\n3

# Strategy Pattern

from abc import ABC, abstractmethod
from random import sample


# Strategy - Interface for sorting algorithms
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


# ConcreteStrategy - Represents Bubble Sort algorithm
class BubbleSort(SortingStrategy):
    def sort(self, data):
        return sorted(data)


# ConcreteStrategy - Represents Quick Sort algorithm
class QuickSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


# ConcreteStrategy - Represents Merge Sort algorithm
class MergeSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        left_sorted = self.sort(left_half)
        right_sorted = self.sort(right_half)
        return self.merge(left_sorted, right_sorted)

    @staticmethod
    def merge(left, right):
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result


# Context - Represents the sorting algorithm context
class SortingContext:
    def __init__(self, sorting_strategy):
        self._sorting_strategy = sorting_strategy

    def set_strategy(self, sorting_strategy):
        self._sorting_strategy = sorting_strategy

    def sort_data(self, data):
        return self._sorting_strategy.sort(data)


# Client Code
if __name__ == "__main__":
    my_data = sample(range(1, 100), 10)

    bubble_sort = BubbleSort()
    quick_sort = QuickSort()
    merge_sort = MergeSort()

    sorting_context = SortingContext(bubble_sort)
    print("Bubble Sort Result:", sorting_context.sort_data(my_data))

    sorting_context.set_strategy(quick_sort)
    print("Quick Sort Result:", sorting_context.sort_data(my_data))

    sorting_context.set_strategy(merge_sort)
    print("Merge Sort Result:", sorting_context.sort_data(my_data))

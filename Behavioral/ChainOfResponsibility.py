# Chain of Responsibility Pattern

from abc import ABC, abstractmethod

# Handler - Interface for handling purchase requests


class PurchaseHandler(ABC):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    @abstractmethod
    def handle_request(self, amount):
        pass

# ConcreteHandler - Represents a manager who can approve purchase requests up to a certain limit


class Manager(PurchaseHandler):
    def __init__(self, name, approval_limit):
        super().__init__()
        self._name = name
        self._approval_limit = approval_limit

    def handle_request(self, amount):
        if amount <= self._approval_limit:
            print(f"{self._name} approved the purchase request of ${amount}")
        elif self._successor is not None:
            self._successor.handle_request(amount)
        else:
            print(f"{self._name} cannot approve the purchase request of ${amount}. Please contact higher management.")


# Client Code
if __name__ == "__main__":
    # Creating managers with different approval limits
    manager1 = Manager("Manager A", 1000)
    manager2 = Manager("Manager B", 3000)
    manager3 = Manager("Manager C", 5000)

    # Chaining the managers together
    manager1.set_successor(manager2)
    manager2.set_successor(manager3)

    # Handling purchase requests
    manager1.handle_request(500)   # Output: Manager A approved the purchase request of $500
    manager1.handle_request(1500)  # Output: Manager B approved the purchase request of $1500
    manager1.handle_request(3500)  # Output: Manager C approved the purchase request of $3500
    manager1.handle_request(6000)  # Output: Manager C cannot approve the purchase request of $6000. 

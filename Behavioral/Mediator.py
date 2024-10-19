# Mediator Pattern

from abc import ABC, abstractmethod


# Mediator - Interface for communication between users
class ChatRoom(ABC):
    @abstractmethod
    def send_message(self, sender, message):
        pass


# ConcreteMediator - Represents the chat room
class TextChatRoom(ChatRoom):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, sender, message):
        for user in self._users:
            if user != sender:
                user.receive_message(sender, message)


# Colleague - Interface for users
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, sender, message):
        pass


# ConcreteColleague - Represents a user in the chat room
class ChatUser(User):
    def __init__(self, name, chat_room):
        super().__init__(name)
        self._chat_room = chat_room

    def send_message(self, message):
        self._chat_room.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received a message from {sender.name}: {message}")


# Client Code
if __name__ == "__main__":
    my_chat_room = TextChatRoom()

    user1 = ChatUser("Alice", my_chat_room)
    user2 = ChatUser("Bob", my_chat_room)
    user3 = ChatUser("Charlie", my_chat_room)

    my_chat_room.add_user(user1)
    my_chat_room.add_user(user2)
    my_chat_room.add_user(user3)

    # Output: Bob received a message from Alice: Hello, everyone!
    #         Charlie received a message from Alice: Hello, everyone!
    user1.send_message("Hello, everyone!")

    # Output: Bob received a message from Charlie: Hi, Alice!
    user3.send_message("Hi, Alice!")

    # Output: Alice received a message from Bob: Greetings!
    #         Charlie received a message from Bob: Greetings!
    user2.send_message("Greetings!")

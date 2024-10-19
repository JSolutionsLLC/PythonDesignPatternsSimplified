# Proxy Pattern

from abc import ABC, abstractmethod


# Subject - Interface for the RealSubject and Proxy
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# RealSubject - Represents the actual image object
class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image from disk: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")


# Proxy - Represents the Image Proxy
class ImageProxy(Image):
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()


# Client Code
if __name__ == "__main__":
    # Real image is loaded immediately
    real_image = RealImage("nature.jpg")
    real_image.display()  # Output: Loading image from disk: nature.jpg\nDisplaying image: nature.jpg

    # Proxy image, real image is loaded only when required
    proxy_image = ImageProxy("architecture.jpg")
    proxy_image.display()  # Output: Loading image from disk: architecture.jpg\nDisplaying image: architecture.jpg

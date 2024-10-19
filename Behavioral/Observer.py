# Observer Pattern

from abc import ABC, abstractmethod


# Observer - Interface for observers
class Investor(ABC):
    @abstractmethod
    def update(self, stock_name, stock_price):
        pass


# ConcreteObserver - Represents an investor observing the stock
class StockInvestor(Investor):
    def __init__(self, name):
        self._name = name

    def update(self, stock_name, stock_price):
        print(f"{self._name} received an update: {stock_name} - {stock_price:.2f}")


# Subject - Interface for the subject being observed
class StockMarket(ABC):
    @abstractmethod
    def add_investor(self, investor):
        pass

    @abstractmethod
    def remove_investor(self, investor):
        pass

    @abstractmethod
    def notify_investors(self, stock_name, stock_price):
        pass


# ConcreteSubject - Represents the stock market and the stock price changes
class StockExchange(StockMarket):
    def __init__(self):
        self._investors = []

    def add_investor(self, investor):
        self._investors.append(investor)

    def remove_investor(self, investor):
        self._investors.remove(investor)

    def notify_investors(self, stock_name, stock_price):
        for investor in self._investors:
            investor.update(stock_name, stock_price)

    def update_stock_price(self, stock_name, stock_price):
        print(f"Stock price update: {stock_name} - {stock_price:.2f}")
        self.notify_investors(stock_name, stock_price)


# Client Code
if __name__ == "__main__":
    stock_exchange = StockExchange()

    investor1 = StockInvestor("John")
    investor2 = StockInvestor("Jane")

    stock_exchange.add_investor(investor1)
    stock_exchange.add_investor(investor2)

    stock_exchange.update_stock_price("ABC", 100.50)
    # Output: Stock price update: ABC - 100.50
    #         John received an update: ABC - 100.50
    #         Jane received an update: ABC - 100.50

    stock_exchange.update_stock_price("XYZ", 75.25)
    # Output: Stock price update: XYZ - 75.25
    #         John received an update: XYZ - 75.25
    #         Jane received an update: XYZ - 75.25

    stock_exchange.remove_investor(investor1)

    stock_exchange.update_stock_price("DEF", 50.75)
    # Output: Stock price update: DEF - 50.75
    #         Jane received an update: DEF - 50.75

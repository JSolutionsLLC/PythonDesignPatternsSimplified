# Interpreter Pattern

from abc import ABC, abstractmethod


# AbstractExpression - Interface for interpreting expressions
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


# TerminalExpression - Represents a number in the expression
class Number(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self):
        return self._value


# NonTerminalExpression - Represents a binary operation in the expression (Addition or Subtraction)
class BinaryOperation(Expression):
    def __init__(self, left_operand, right_operand, operator):
        self._left_operand = left_operand
        self._right_operand = right_operand
        self._operator = operator

    def interpret(self):
        if self._operator == "+":
            return self._left_operand.interpret() + self._right_operand.interpret()
        elif self._operator == "-":
            return self._left_operand.interpret() - self._right_operand.interpret()
        else:
            raise ValueError("Invalid operator.")


# Client Code
if __name__ == "__main__":
    # Representing the expression: 3 + 2 - 1
    expression = BinaryOperation(BinaryOperation(Number(3), Number(2), "+"), Number(1), "-")

    result = expression.interpret()
    print("Result:", result)  # Output: Result: 4

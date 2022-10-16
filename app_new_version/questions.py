from collections import namedtuple
import random

NumRange = namedtuple('NumRange', ['start', 'end'], defaults=[0, 0])


class Question:
    pass


class MathQuestion(Question):

    def __init__(self, first_operand: int = None, operation: str = None, second_operand: int = None):
        """Not supposed to be called directly mostly. Use generate method instead for math quiz"""
        self.first_operand = first_operand
        self.operation = operation
        self.second_operand = second_operand

    def __str__(self):
        return f"{self.first_operand} {self.operation if self.operation != '**' else ''}" \
               f" {self.second_operand if self.second_operand else ''}"

    @staticmethod
    def generate(start: int | NumRange, end: int | NumRange, operations: list[str]):
        """Accepts start as int or NumRange, end as int, NumRange and operations. If start or operation
            is not of a correct type assertion error will be thrown in the end. """
        first_operand, second_operand = None, None
        if isinstance(start, NumRange) and isinstance(end, NumRange):
            first_operand = random.randint(start.start, start.end)
            second_operand = random.randint(end.start, end.end)
        elif isinstance(start, int) and isinstance(end, int):
            first_operand = random.randint(start, end)
            second_operand = random.randint(start, end)
        operation = random.choice(operations)
        assert first_operand and operation, f'Failed. 1 operand {first_operand}. Operation: {operation}. ' \
                                            f'Expected {MathQuestion.generate.__doc__}'
        return MathQuestion(first_operand, operation, second_operand)

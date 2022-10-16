import operator


class Calculator:
    operations_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '**': operator.pow}

    @staticmethod
    def calculate(first_operand: int | float, operation: str, second_operand: int | float) -> int | None:
        calc = Calculator.operations_dict.get(operation)
        if not calc:
            print(f'Operation is not available. Given {operation}. Available: {Calculator.operations_dict.keys()}')
        else:
            return calc(first_operand, 2) if operation == '**' else calc(first_operand, second_operand)

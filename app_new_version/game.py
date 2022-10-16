from level import Level, Question
import time
from calculator import Calculator


def timer(scope='task'):
    def wrapper_outside(function):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = function(*args, **kwargs)
            print(f'It took {round(time.perf_counter() - start, 2)} seconds for you to complete this {scope}')
            return result
        return wrapper
    return wrapper_outside


class Game:

    def __init__(self) -> None:
        self.levels = {}
        self.__score = 0

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, increase_on: int) -> None:
        self.__score += increase_on     # increases the score by a given number

    def add_level(self, level: Level) -> None:
        if isinstance(level, Level):
            self.levels.setdefault(level.complexity, level)
        else:
            print(f"Sorry, level should be an instance of <class 'Level'>. Given {type(level)}")

    @timer()
    def ask_question(self, question: Question) -> None:
        print(question)
        user_answer = read_user_input(input_text='Enter your answer: ', error_text='Wrong format! Try again.')
        is_correct = self.check_answer(Calculator.calculate, user_answer, first_operand=question.first_operand,
                                       operation=question.operation, second_operand=question.second_operand)
        # TODO result checker set as a attribute of instance and call it
        if not is_correct:
            print('Wrong')
        else:
            print('Right!')
            self.score = 1

    @staticmethod
    def check_answer(check_function,  user_answer, *args, **kwargs) -> bool:
        result = check_function(*args, **kwargs)
        return result == user_answer

    @timer(scope='level')
    def start(self, level: Level) -> None:
        for question in level.questions:
            self.ask_question(question)


def read_user_input(input_text: str = '', error_text: str = None) -> int:
    while True:
        try:
            user_answer = int(input(input_text))
            return user_answer
        except ValueError:
            print(error_text if error_text else '', end='')

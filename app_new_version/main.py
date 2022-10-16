import random
import os
from game import Game, read_user_input
from level import Level
from questions import MathQuestion, NumRange, Question


class User:

    def __init__(self):
        self.__name = input('What is your name?\n')

    @property
    def name(self):
        return self.__name


class FileSaver:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.file_size = os.path.getsize(self.filepath) if os.path.exists(self.filepath) else None

    def save(self, string: str) -> None:
        with open(self.filepath, 'a+', encoding='utf-8') as f_out:
            print(string, file=f_out)
            print(f'The results are saved in {self.filepath}')

    def read_file(self) -> list | None:
        with open(self.filepath) as f_in:
            data = f_in.readlines()
            return data


def square_integral_gen(start: int, end: int):
    question = MathQuestion()
    question.first_operand = random.randint(start, end)
    question.operation = '**'
    return question


def print_levels(game_levels: list) -> None:
    for lvl in game_levels:
        print(lvl)


def print_previous_results() -> None:
    try:
        reader = FileSaver('results.txt')
        data = reader.read_file()
        if reader.file_size == 0:
            print('Your results file is empty')
        else:
            print('Printing your previous results:')
            for ind, line in enumerate(data, 1):
                print(f"{ind}. {line.strip()}")
    except FileNotFoundError:
        print('You don\'t have any previous results:(')


def save_results(game_score: int, num_of_questions: int, complexity_lvl: str):
    is_to_save_result = input("Would you like to save your result to the file? Enter yes or no.\n").lower()
    while is_to_save_result not in ['yes', 'no', 'y', 'n']:
        print('Wrong format!')
        is_to_save_result = input("Would you like to save your result to the file? Enter yes or no.\n").lower()
    if is_to_save_result in ['yes', 'y']:
        user = User()
        FileSaver('results.txt').save(f'{user.name.title()}: {game_score}/{num_of_questions} in level {complexity_lvl}')
    else:
        print('Bye. See you later!')


def setup_levels() -> list[Level]:
    level_1 = Level(complexity=1, name="simple operations with numbers 2-9 (7 seconds to complete every task)")
    level_2 = Level(complexity=2, name="integral squares of 11-29 (12 seconds to complete every task)")
    level_3 = Level(complexity=3,
                    name="adding and subtracting with numbers 100-1000 (15 seconds to complete every task)")
    level_4 = Level(complexity=4, name="multiplication of 10-99 by 2-9 (20 seconds to complete every task)")
    level_1.setup(MathQuestion.generate, start=2, end=9, operations=['+', '-', '*'])
    level_2.setup(square_integral_gen, start=11, end=29)
    level_3.setup(MathQuestion.generate, start=100, end=1000, operations=['+', '-'])
    level_4.setup(MathQuestion.generate, start=NumRange(10, 99), end=NumRange(2, 9), operations=["*"])
    return [level_1, level_2, level_3, level_4]


def main():
    print_previous_results()
    levels = setup_levels()
    game = Game()
    for lvl in levels:
        game.add_level(lvl)
    print('Which level do you want? Enter a number:\n')
    print_levels(game.levels.values())
    user_input = read_user_input(error_text='Wrong format\n')
    level_to_run: Level = game.levels.get(user_input)
    if not level_to_run:
        print('Wrong option')
    else:
        game.start(level_to_run)
        print(f'Your score is {game.score}/{level_to_run.num_of_questions}')
        save_results(game.score, level_to_run.num_of_questions, f'{level_to_run.complexity} {level_to_run.name}')


if __name__ == "__main__":
    main()

import random


def calculations():
    inputs = [x for x in range(2, 10)]
    operations = ['*', '-', '+']
    first_operand = random.choice(inputs)
    operation = random.choice(operations)
    second_operand = random.choice(inputs)
    return first_operand, operation, second_operand


def calculation_logic(first_operand, operation, second_operand):
    result = 0
    if operation == '+':
        result = first_operand + second_operand
    elif operation == '-':
        result = first_operand - second_operand
    elif operation == '*':
        result = first_operand * second_operand
    else:
        print('Wrong input')
    return result


def integral_calculation():
    number_to_calc = random.choice(range(11, 30))
    print(number_to_calc)
    result = number_to_calc ** 2
    return result


def check_user_calc_result(user_result, actual_result):
    if user_result == actual_result:
        return 'Right!'
    return 'Wrong'


def choose_option(option):
    if option == 1:
        first_operand, operation, second_operand = calculations()
        print(str(first_operand), operation, str(second_operand))
        result = calculation_logic(first_operand, operation, second_operand)
        return result
    elif option == 2:
        result = integral_calculation()
        return result


def ask_user_answer():
    try:
        user_answer = int(input())
    except ValueError:
        print('Wrong format! Try again.')
        return ask_user_answer()
    return user_answer


def select_option():
    try:
        user_answer = int(input("Which level do you want? Enter a number: \n"
                                "1 - simple operations with numbers 2-9 \n"
                                "2 - integral squares of 11-29 \n"))
        if user_answer not in [1, 2]:
            raise ValueError
    except ValueError:
        print('Incorrect format.')
        return select_option()
    return user_answer


def saving_results_to_file(game_score, lvl):
    answer = input("Would you like to save your result to the file? Enter yes or no.\n").lower()
    if answer == "yes" or answer == 'y':
        user_name = input('What is your name?\n')
        results_file = open('results.txt', 'a', encoding='utf-8')
        results_file.write(user_name + ': ' + str(game_score) + '/5' + ' in level ' + str(lvl) + '\n')
        results_file.close()
        print('The results are saved in "results.txt"')
        return ''
    else:
        exit()


def game_session():
    questions = 5
    game_score = 0
    user_option = select_option()
    if user_option == 1:
        lvl = "1 (simple operations with numbers 2-9)."
    else:
        lvl = "2  (integral squares of 11-29)."
    while questions:
        result = choose_option(user_option)

        user_answer = ask_user_answer()
        print(check_user_calc_result(user_answer, result))
        if user_answer == result:
            game_score += 1
        questions -= 1
    print(f'Your mark is {game_score}/5.')
    return saving_results_to_file(game_score, lvl)


print(game_session())

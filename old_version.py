def calculations():
    inputs = [x for x in range(2, 10)]
    operations = ['*', '-', '+']
    first_operand = random.choice(inputs)
    operation = random.choice(operations)
    second_operand = random.choice(inputs)
    return first_operand, operation, second_operand


def calculation_logic(first_operand, operation, second_operand):
    operations_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    print(str(first_operand), operation, str(second_operand))
    calc = operations_dict.get(operation)
    if not calc:
        print('Wrong input')
    return 0 if not calc else calc(first_operand, second_operand)


def adding_and_subtraction_100_1000():
    operations = ['-', '+']
    first_operand = random.choice(range(100, 1001))
    second_operand = random.choice(range(100, 1001))
    operation = random.choice(operations)
    return first_operand, operation, second_operand


def multiplication_10_100_by_2_10():
    first_operand = random.choice(range(10, 100))
    second_operand = random.choice(range(2, 10))
    operation = '*'
    return first_operand, operation, second_operand


def integral_calculation():
    number_to_calc = random.choice(range(11, 30))
    print(number_to_calc)
    result = number_to_calc ** 2
    return result


def check_user_calc_result(user_result, actual_result, check_time_result):
    if user_result == actual_result:
        if check_time_result is True:
            return 'Right!'
        else:
            return 'The answer is right, but you failed the deadline'
    return 'Wrong'


def choose_option(option):
    if option == 1:
        first_operand, operation, second_operand = calculations()
        result = calculation_logic(first_operand, operation, second_operand)
    elif option == 2:
        result = integral_calculation()
    elif option == 3:
        first_operand, operation, second_operand = adding_and_subtraction_100_1000()
        result = calculation_logic(first_operand, operation, second_operand)
    else:
        first_operand, operation, second_operand = multiplication_10_100_by_2_10()
        result = calculation_logic(first_operand, operation, second_operand)
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
                                "1 - simple operations with numbers 2-9 (7 seconds to complete every task) \n"
                                "2 - integral squares of 11-29 (12 seconds to complete every task)\n"
                                "3 - adding and subtracting with numbers 100-1000 (15 seconds to complete every task)\n"
                                "4 - multiplication of 10-99 by 2-9 (20 seconds to complete every task)\n"))
        if user_answer not in [1, 2, 3, 4]:
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
    elif answer == 'no':
        return 'Bye. See you later!'
    else:
        print('Wrong format!')
        return saving_results_to_file(game_score, lvl)


def check_previous_user_results():
    try:
        read = open('results.txt', encoding='utf-8')
        file_size = os.path.getsize('results.txt')
        if file_size == 0:
            print('Your results file is empty')
        else:
            print('Printing your previous results:')
            i = 1
            for line in read.readlines():
                print(str(i) + '.', line, end='')
                i += 1
    except FileNotFoundError:
        print('You don\'t have any previous results:(')



def printing_chosen_lvl(user_option):
    if user_option == 1:
        lvl = "1 (simple operations with numbers 2-9)."
    elif user_option == 2:
        lvl = "2  (integral squares of 11-29)."
    elif user_option == 3:
        lvl = "3 - adding and subtracting with numbers 100-1000."
    else:
        lvl = "multiplication of 10-99 by 2-9"
    return lvl


def time_difference_check(time_difference, time_required):
    if time_difference <= time_required:
        return True
    return False


def check_time(user_option, final_time):
    if user_option == 1:
        time_required = 7.0
        check_result = time_difference_check(final_time, time_required)
    elif user_option == 2:
        time_required = 12.0
        check_result = time_difference_check(final_time, time_required)
    elif user_option == 3:
        time_required = 15.0
        check_result = time_difference_check(final_time, time_required)
    else:
        time_required = 20.0
        check_result = time_difference_check(final_time, time_required)
    return check_result


def current_game_start_parameters():
    questions = 5
    game_score = 0
    total_time = 0
    return questions, game_score, total_time


def main():
    questions, game_score, total_time = current_game_start_parameters()
    check_previous_user_results()
    user_option = select_option()
    lvl = printing_chosen_lvl(user_option)
    while questions:
        result = choose_option(user_option)
        start_time = time.perf_counter()
        print('Time counting started')
        user_answer = ask_user_answer()
        finish_time = time.perf_counter()
        total_time += round(finish_time - start_time, 2)
        time_difference = round(finish_time - start_time, 2)
        check_time_result = check_time(user_option, time_difference)
        print(f'It took {time_difference} seconds for you to solve this task')
        print(check_user_calc_result(user_answer, result, check_time_result))
        if user_answer == result and check_time_result is True:
            game_score += 1
        questions -= 1
    print(f'You finished the lvl {lvl} in {total_time}')
    print(f'Your mark is {game_score}/5.')
    return saving_results_to_file(game_score, lvl)


if __name__ == "__main__":
    print(main())

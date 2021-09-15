# exam_calculator
simple app that asks math tasks and checks user answers


## Stage 4/4: Adding marks
### Description
Simple tasks are good for younger kids, but math can be more difficult and more interesting! Quadratic equations, trigonometry, and a lot of other interesting things. Math library can help you with that.

Sometimes students want to save the results of the test. This is useful for viewing the learning dynamics on a topic or to identify difficult tasks.

At this stage, let's add integral squares. Of course, you can add more difficulty levels later.

### Objectives
- [x] With the first message, the program should ask for a difficulty level:
    - [x] 1 - simple operations with numbers 2-9
    - [x] 2 - integral squares 11-29

- [x] A user enters an answer.
    - [x] For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
    - [x] For the second difficulty level: the task is an integer; the answer is the square of this number.
    - [x] In case of another input: ask to re-enter. Repeat until the format is correct.

- [x] The application gives 5 tasks to a user.

- [x] The user receives one task, prints the answer.
    - [x] If the answer contains a typo, print Incorrect format. and ask to re-enter the answer. Repeat until the answer is in the correct format.
    - [x] If the answer is a number, print Right! or Wrong! Go to the next question.

- [x] After five answers, print Your mark is N/5. where N is the number of correct answers.

- [x] Output Would you like to save your result to the file? Enter yes or no.
    - [x] In case of yes, YES, y, Yes: the app should ask the username and write Name: n/5 in level X (<level description>). (X stands for the level number) in the results.txt file. For example — Alex: 3/5 in level 1 (simple operations with numbers 2-9).
    - [x] The results should be saved to the file immediately after the user gave the positive answer to the question Would you like to save your result to the file?
    - [x] If the file results.txt does not exist, you should create it.

- [x] In case of no or any other word: exit the program.

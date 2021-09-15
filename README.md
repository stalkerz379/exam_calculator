# Arithmetic Exam Application
## Stage 1: Mini-calculator

### Description
People learn new things in one way or another. Learning sometimes means that you need to check your comprehension by taking a test. It also requires a person (or a program) to check your answers. You may have been in a situation when you think that you have solved the task correctly, but your professor has a different (sometimes wrong!) answer. It happens; everybody makes mistakes.

Not our application though. It should calculate the solution in a very precise manner. We need to make a simple calculator that can evaluate expressions like **a + b, a - b, or a * b**

### Objectives
- [x] A user inputs a line that looks like a simple mathematical operation.
- [x] The application should print the result of the operation.

## Stage 2: Task generator

### Description
Any test includes at least one task. This task can vary in difficulty and required timeframes. There can be more than one task; they can demand different forms of answers. One thing remains — if there's a task, there's a solution. And we need to assess it.

For now, let's use random numbers from **2 to 9** and integer operations: **'+, - and *'**.

### Objectives
- [x] Generate a math task that looks like a math operation. Use the requirements above. Print it.
- [x] Read the answer from a user.
- [x] Check whether the answer is correct. Print **Right!** or **Wrong!**

## Stage 3: More tasks needed!

### Description
Let's write an application that assesses the user's knowledge.
Many people get nervous during exams; they can accidentally hit a wrong key, confuse , with . in floats, and so on. Our application should allow some room for errors and give a person the opportunity to correct the typo.

### Objectives
- [x] The application should give the user **5 tasks**. The tasks are akin to the previous stage: two numbers from **2 to 9** and an **integer operation**.
- [x] The user receives one task, prints the answer. If the answer contains a typo (letters or otherwise empty), the program should print **Incorrect format.** and ask to re-enter the answer. Repeat until the answer is in the correct format. If the answer is a number, print **Right!** or **Wrong!** depending on the answer and carry on to the next question.
- [x] After five tasks, output **Your mark is n/5**. where n is the number of correct answers.

## Stage 4/4: Adding marks
### Description
Simple tasks are good for younger kids, but math can be more difficult and more interesting! Quadratic equations, trigonometry, and a lot of other interesting things. Math library can help you with that.

Sometimes students want to save the results of the test. This is useful for viewing the learning dynamics on a topic or to identify difficult tasks.

At this stage, let's add integral squares. Of course, you can add more difficulty levels later.

### Objectives
- [x] With the first message, the program should ask for a difficulty level:
    - [x] **1 - simple operations with numbers 2-9**
    - [x] **2 - integral squares 11-29**

- [x] A user enters an answer.
    - [x] For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
    - [x] For the second difficulty level: the task is an integer; the answer is the square of this number.
    - [x] In case of another input: ask to re-enter. Repeat until the format is correct.

- [x] The application gives 5 tasks to a user.

- [x] The user receives one task, prints the answer.
    - [x] If the answer contains a typo, print **Incorrect format.** and ask to re-enter the answer. Repeat until the answer is in the correct format.
    - [x] If the answer is a number, print **Right!** or **Wrong!**. Go to the next question.

- [x] After five answers, print **Your mark is N/5.** where N is the number of correct answers.

- [x] Output **Would you like to save your result to the file? Enter yes or no.**
    - [x] In case of **yes**, **YES**, **y**, **Yes**: the app should ask the username and write **Name: n/5 in level X (<level description>).** (X stands for the level number) in the **results.txt file.** For example — **Alex: 3/5 in level 1 (simple operations with numbers 2-9).**
    - [x] The results should be saved to the file immediately after the user gave the positive answer to the question **Would you like to save your result to the file?**
    - [x] If the file **results.txt** does not exist, you should create it.

- [x] In case of **no** or **any other word**: exit the program.

## Sample ideas how to improve the application:

1. Add a complex exam. Increase a difficulty level on the fly. For example, if a person passed the 1st level, start the 2nd one immediately.
2. You can add a correction level: store the tasks with wrong answers and give them next time.
- [x] ~~3. Add more difficulty levels.~~ **added 2 new lvlv**
4. Track the time (read about Timer).
5. Write a more detailed report to a file with the results.
6. Show previous results inside the app (show lines from results.txt that contains the username)
7. Any other improvement that might be useful!

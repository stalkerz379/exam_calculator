from questions import Question, MathQuestion


class Level:

    def __init__(self, complexity: int, name: str, num_of_questions: int = 5) -> None:
        self.complexity = complexity
        self.name = name
        self.num_of_questions = num_of_questions
        self.questions = []

    def __str__(self) -> str:
        return f"{self.complexity} - {self.name}"

    def setup(self, function, *args, **kwargs) -> None:
        """Method used to generate questions in range of num_of_questions. Calls method generate of MathQuestion class
        to generate questions. Appends question to the list of questions. If function is given it should generate
        questions of class MathQuestion. Can accept function as argument with arguments"""
        for _ in range(self.num_of_questions):
            question = function(*args, **kwargs)
            if isinstance(question, Question):
                self.questions.append(question)

    def add_question(self, question: Question) -> None:
        if isinstance(question, Question):
            self.questions.append(question)
        else:
            print(f'Error. The question should be an instance of <class MathQuestion>. Given {type(question)}')


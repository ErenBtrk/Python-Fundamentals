# Question Class

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

    
q1 = Question("Which is the best programming language?",["C#","Python","Javascript","C++"],"python")
q2 = Question("Which is the main programming language of Unreal Engine?",["C#","Python","Javascript","C++"],"c++")
q3 = Question("Which is the central city of Turkey?",["Istanbul","Izmir","Ankara","Corum"],"ankara")
q4 = Question("Which one of the basketball players has more scoring leader award?",["Kevin Durant","Michael Jordan","Lebron James","Kobe Bryant"],"michaeljordan")
q5 = Question("Who is the owner of space-X?",["Einstein","Jeff Bezos","Bill Gates","Elon Musk"],"elonmusk")

# Quiz Class

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Your Answer : ").lower().replace(" ","")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
            print("YOUR ANSWER IS RIGHT! :)")
        else:
            print("YOUR ANSWER IS WRONG :(")
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()


    def showScore(self):
        print(f"Your score is : {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz is ended.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))

question_list = [q1,q2,q3,q4,q5]

quiz = Quiz(question_list)

quiz.loadQuestion()
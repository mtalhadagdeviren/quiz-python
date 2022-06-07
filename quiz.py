#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self, answer):
        return self.answer == answer

#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question= self.getQuestion()
        #self.questionIndex Soru 1 şeklinde yansıyacak
        print(f'Soru {self.questionIndex+1} : {question.text}')
        
        for q in question.choices:
            print('*' + q)
        
        answer= input('Answer: ')
        self.questionGuess(answer)
        self.loadQuestion() 
    
    def questionGuess(self,answer):
        question = self.getQuestion()
        if(question.checkAnswer(answer)):
            self.score +=20
        self.questionIndex +=1
    
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.progress()
            self.displayQuestion()
    
    def showScore(self):
        print(f'Skorunuz:{self.score}')
    
    def progress(self):
        totalQuestion = len(self.questions)
        questionNo = self.questionIndex + 1
        if(questionNo > totalQuestion):
            print('sınav bitti')
        else:
            print(f'Question {questionNo} of {totalQuestion}')




q1=Question('ABC',['1','2','3','4'],3)
q2=Question('DEF',['1','2','3','4'],4)
sorular=[q1,q2]
quiz=Quiz(sorular)
s1=quiz.loadQuestion()

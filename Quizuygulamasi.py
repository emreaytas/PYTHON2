class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer # doğru ise True değilse False dönecek böylece.
        
     
q1 = Question('En iyi programlama dili hangisidir?',['C#','Java','Javascript','python'],'python')
q2 = Question('En yavaş programlama dili hangisidir?',['C#','Java','Javascript','python'],'python')
q3 = Question('En populer dili hangisidir?',['C#','Java','Javascript','python'],'javascript')
 
questions = [q1,q2,q3]      

class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex] 
    
    def displayQuestion(self):
        question = self.getQuestion()
        self.questionIndex += 1
        print(f"Soru {self.questionIndex}: {question.text}")
        
        for q in question.choices:
            print("-"+q)
        
        answer = input("Cevabi giriniz: ")
    
        
    
quiz = Quiz(questions)

           
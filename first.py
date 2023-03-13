class Person():
    def __init__(self):
        print('Person Created.')

class Student(Person):
    def __init__(self):
        super().__init__(self)
        print("Student created.")
        
                 
         
import pymysql as sql
from datetime import datetime

connection = sql.connect(
         host = "localhost",
         password = "12345",
         user= "root",
         database = "emre"        
      )


class Student():
    
    def __init__(self,id,studentnumber,name,surname,birthdate,gender,classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentnumber = studentnumber
        if len(name) > 45:
            raise Exception("name icin maksimum 45 karakter girmelisiniz...")
        else:
            self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid
    
    @staticmethod
    def createStudent(obj):
        liste = []
        
        if isinstance(obj,tuple):    # isinstance ile bir bir yapının türünü belirleyebiliriz.
            liste.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                liste.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        
        return liste 
       
class Teacher():
    
    def __init__(self,id,branch,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

class Lesson():
    
    def __init__(self,id,name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name

class Class():
    
    def __init__(self,id,name,teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid
        
class ClassLesson():
    
    def __init__(self,classid,lessonid,teacherid):
        self.classid = classid
        self.lessonid = lessonid
        self.teacherid = teacherid        
      
      
        
class DbManager():
    def __init__(self,connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def addStudent(self,student:Student): # bir class geleceği için tipini belirttik.
        pass    
    def editStudent(self,student:Student):
        pass    
    
    def addTeacher(self,teacher:Teacher): # bir class geleceği için tipini belirttik.
        pass    
    
    def editTeacher(self,teacher:Teacher):
        pass    
    
    def getStudentById(self,id):
        sql = "select * from student where id = %s"
        value = (id,)  # tek bir value varsa o zaman (deger,) şeklinde olmalı.
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.createStudent(obj)
        except:
            print("...")
            
    def getStudentByClassid(self,id):
        sql = "select * from student where classid = %s"
        value = (id,)  # tek bir value varsa o zaman (deger,) şeklinde olmalı.
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)  #static metotun return ettiğini return eder bu sistem.
        except:
            print("...")
            
                  
db =  DbManager(connection)
student = db.getStudentById(7)
   







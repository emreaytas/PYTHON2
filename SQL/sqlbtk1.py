import pymysql
import datetime

def createStudent():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
CREATE TABLE if not exists emre`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(5) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `birthdate` DATETIME NOT NULL,
  `gender` VARCHAR(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `number_UNIQUE` (`number` ASC) VISIBLE);

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()    
    
def createTeacher():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
    CREATE TABLE if not exists `emre`.`teacher` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `branch` VARCHAR(20) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `birthdate` DATETIME NOT NULL,
  `gender` VARCHAR(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()    

def createClass():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
CREATE TABLE if not exists `emre`.`class` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`));

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()    

def createLesson():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
CREATE TABLE if not exists `emre`.`lesson` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`));

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()  

def Alter1():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
    alter table 'emre'.student add column 'classid' int not null after 'gender'

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()          

def classLesson():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
CREATE TABLE if not exists `emre`.`classlesson` (
  `classid` INT NOT NULL,
  `lessonid` INT NOT NULL,
  `teacherid` INT NOT NULL,
  PRIMARY KEY (`classid`, `lessonid`, `teacherid`));
                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()             

def Alter2():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
    alter table 'emre'.'class' add constraint fk_teacher_class foreign key(teacherid) references teacher(id)

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()      
                
def Alter3():
    connection = pymysql.connect(
        host = "localhost",
        password = "12345",
        database = "emre",
        user = "root"           
    )
    
    cursor = connection.cursor()
    
    cursor.execute("""
                   
    alter table 'emre'.'student' add constraint fk_student_class foreign key(classid) references class(id)

                   """) 
    
    try:
        
        connection.commit()
        
    except pymysql.Error as err:
        print(err)
    
    finally:
        connection.close()        
        
createTeacher()
createStudent()
createClass()
createLesson()
Alter1()
classLesson()
Alter2()
Alter3()



        
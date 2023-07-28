import pymysql as sql
import datetime

def createTable1():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
  
  CREATE TABLE if not exists `emre`.`teacher` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `branch` VARCHAR(30) NULL,
  `name` VARCHAR(25) NULL,
  `surname` VARCHAR(45) NULL,
  `birthdate` DATETIME NULL,
  `gender` VARCHAR(1) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
                 
                       
                       
                       
                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()
    

def createTable2():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
                       
  CREATE TABLE if not exists `emre`.`class` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `classcol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
                            
                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()
    

def createTable3():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
    CREATE TABLE if not exists `emre`.`lesson` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

                    
                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()
 
def createTable4():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
  CREATE TABLE if not exists `emre`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `birthdate` DATETIME NULL,
  `gender` VARCHAR(1) NULL,
  `classid` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
  


                    
                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()    


def AlterTable1():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )

    
    try:
        cursor = connection.cursor()
        cursor.execute("""alter table student add column classid int not null""")
        
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()

def AlterTable2():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )

    
    try:
        cursor = connection.cursor()
        cursor.execute("""
                       alter table class add column teacherid int not null
                       """)
        
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()

def createTable5():
    
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""

CREATE TABLE if not exists `emre`.`classlesson` (
  `classid` INT NOT NULL,
  `lessonid` INT NOT NULL,
  `classlessoncol` INT NOT NULL,
  PRIMARY KEY (`classid`, `lessonid`, `classlessoncol`));

                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()    

def createForeign1():
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
             alter table class 
             add constraint fk_class_teacher
             foreign key (teacherid) references teacher(id)    

                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()    

def createForeign2():
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
                       
             alter table student
             add constraint fk_student_class
             foreign key (classid) references class(id)    

                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()        

createTable1()
createTable2()
createTable3()
createTable4()
AlterTable1()
AlterTable2()
createTable5()
createForeign1()
createForeign2()

def createForeign3():
    connection = sql.connect(
       database= "emre",   # database belirttik böylece use emre demeye gerek kalmadı.
       password="12345",
       user = "root",
       host="localhost"
    )
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
                      drop table * 
                       """)
    except sql.Error as e:
        print(e)
    finally:
        connection.commit()
        connection.close()        


createForeign3()











class Person():
    def __init__(self,name,surname):
        self.name = name
        self.surname
    
    
def listeTekle(list1):
    liste2 = []
    for i in list1:
        if i in liste2:
            continue
        else:
            liste2.append(i)
    return liste2
          
"""
    import second
    liste = ["3","33","2","fdfddf",2343,21423,"edffff",342]
    list1 = second.sadeceSayilar(liste)
    print(list1) #['3', '33', '2', 2343, 21423, 342]
"""
def sadeceSayilar(x):
    y = []
    for i in x:
        try:
            value = int(i)
            y.append(i)
        except:
            continue    
    return y

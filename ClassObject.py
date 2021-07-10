class Person:
    def __init__(self,fname,lname):
        self.fn = fname
        self.ln = lname

    def info(crap):
        print(crap.fn, crap.ln)
class Student(Person):
    def __init__(dop,first,last,clas):
        Person.__init__(dop,first,last)
        dop.gradyear = 2020
        dop.clas = clas
    def byebye(lame):
        print("ByeBye",lame.fn,lame.ln,"of class",lame.clas,"of",lame.gradyear)

p1 = Person("John","Doe")
p1.info()
p1.fn = "Baby"
p1.info()
x = Student("Jhonny","Depp",11)
x.info()
x.byebye()

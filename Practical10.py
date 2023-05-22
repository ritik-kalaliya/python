class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
            print(self.name)
            print(self.age)
class student(person):
    def __init__(self,name,age,rollno):
      self.rollno=rollno
      person.__init__(self,name,age)
    def disp(self):
        print(self.name)
        print(self.rollno)
p=person('ABC',23)
p.disp()
s=student('XYZ',24,2468)
s.disp()
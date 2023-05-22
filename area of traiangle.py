print("Name: RITIK\nRoll No.: 25513\nBranch: ECS") 
class Triangle:
 def __init__(self,a,b,c): 
   self.a = a
   self.b = b
   self.c = c 
   def area(self):
    s = (self.a + self.b + self.c) / 2
    area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
    print(f"The area of the triangle is {area:.2f} square units.")
tri = Triangle(3,4,5) 
tri.area()



class Student:
   college_name = "ABC College"
   name = "anonymous"#class atribute

   def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("adding new student in Database .. ")

s1 = Student("karan", 97)
print(s1.name) # -> obj att > class attr
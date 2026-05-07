# creating class
class student:

    #default constructor
    def __init__(self):
        pass
    
    #parameterised constructor
    def __init__(self,fullname ):
        # print(self)
        self.name = fullname

        print("addding new student in database")

    

#creating object (instance)
s1 = student("muskan")
# print(s1) internally self ka yahi matlb h.
print(s1.name)

s2 = student("stuti")
print(s2.name)
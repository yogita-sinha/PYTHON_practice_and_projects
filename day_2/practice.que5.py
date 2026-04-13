a=int(input("enter 1 number:")) 
b=int(input("enter 2 number:")) 
c=int(input("enter 3 number:")) 
d=int(input("enter 4 number:"))
if(a>=b and a>=c and a>=d):
    print("a is greatest number",a)

elif(b>=c and b>=d ):
    print("b is greatest number",b)

elif(c>=d):
    print("c is greatest number",c)

else:
    print("d is greatest number",d)
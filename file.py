

f = open("demo.txt" , "r") 
# this function is used to open a file and it takes two arguments

data = f.read() 
# this function is used to read the contents of a file and it returns the contents of the file as a string.
print(data)
line1 = f.readline()
# this function is used to read a single line from a file and it returns the line as a string.
line2 = f.readline()

print(line1)
# this function is used to print the contents of a line read from a file.
print(line2)
# this function is used to print the contents of a line read from a file.

# print(data) 
# # this function is used to print the contents of a file.

# print(type(data)) 
# # this function is used to print the type of the data variable.

f.close() 
# this function is used to close a file and it is important to close a file after performing operations on it.    

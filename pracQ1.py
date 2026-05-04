cities = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Kolkata"]
heroes = ["Superman", "Batman", "Spiderman", "Ironman", "Thor"]

#WAF to print the length of a list .(list is the parameter)
def print_len(list):
    print(len(list))

print_len(cities)

#write a function to print the items of a list in a single line with space as a separator. (list is the parameter)
def print_list(list):
    for item in list:
        print(item , end = " ")

        
print_list(heroes)

#WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact, end = "\n")
   
factorial(5) 

#WAF to convert USD to INR. (USD is the parameter)
def converter (usd):
    inr = usd*89
    print(usd,"USD = ", inr , "INR")

converter (100)    


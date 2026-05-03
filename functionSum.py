def calc_sum (a,b,c):
    sum = a+b+c
    
    return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = calc_sum(num1, num2, num3)
print("The sum is:", result)
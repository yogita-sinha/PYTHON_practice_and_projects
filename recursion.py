def show(n):
    if (n == 0): #base case -> important for recursion to avoid infinite loop
        return
    print(n)
    show(n-1)
    print("end")

show(5) 

#call stack
#show(5) -> show(4) -> show(3) -> show(2) -> show(1) -> show(0) -> return

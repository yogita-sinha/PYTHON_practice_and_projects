def printList(list , idx ):
    if (idx == len(list)):
        return 
    else :
        print (list[idx])
        printList(list , idx+1)

fruits = ["apple", "banana", "grapes", "orange", "kiwi"]
printList(fruits , 0) #index ki starting point 0 se hoti hai.       
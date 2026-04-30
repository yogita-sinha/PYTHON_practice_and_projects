list = [1 ,4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]

x = 64
print(list)
print("finding",x)
for num in list:
    
    if(num == x):
       
        print("found at index :" , list.index(num))
        break
    else:
        print ("finding...")    
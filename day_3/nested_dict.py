student = {
    "name":"yogita sinha",
    "subject" : {
        "physics" : 91,
        "chemistry" : 89,
        "maths" : 95,   

    }
}
#nested dictionary
print (student)
print (student["subject"])
print ("physics:" + str(student["subject"]["physics"]))

#methods
#keys() number of keys in the dictionary
print( "keys of the dictionary:" + str(list(student.keys())))

#length of the dictionary
print( "length of the dictionary:" + str(len(student)))

#values() number of values in the dictionary
print( "values of the dictionary:" + str(list(student.values()))) 

#items() number of key value pairs in the dictionary
print( "items of the dictionary:" + str(list(student.items())))

pairs = list(student.items())
print(pairs[0])

#.get() method to access value of a key
print(student["name"])
print(student.get("name"))

#print(student["name2"]) #error because name2 is not present in the dictionary
print(student.get("name2")) #it will return none because name2 is not present in the dictionary
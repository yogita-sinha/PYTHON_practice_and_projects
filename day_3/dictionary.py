info = {
    "name": "yogita",
    "age": 20,
    "is_adult": "true",
    "subjects":["maths", "science", "english"],
    "marks": [90, 85, 92],
    "topics":("dictionary","set","list","tuple"),
}

print(type(info))
print(info["name"])
print(info["age"])
print(info["is_adult"])     
print(info["subjects"])
print(info["marks"])
print(info["topics"])

info["name"] = "muskan"
print(info["name"])

null_dict = {}
print(null_dict)

null_dict["name"]="richita"
print(null_dict )
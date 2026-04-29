# set.add(el) // adds an element to the set
# set.clear() // empties the sets
# set.pop() // remove random value
# set.remove(el) // removes the element an

#sets are mutable , but the elements of the set is immutable.

collection = set ()
collection.add(1)
collection.add(2)       
print(collection)
collection.add(3)   
collection.remove(2)
print(collection)
collection.add("muskansinha")
print(collection)

#set.union(set1,set2) combine both sets value and return new
#set.intersection(set1,set2) return common value in both sets

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
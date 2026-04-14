#polindrome number

from shutil import copy


org = [1,2,3,2,1]
copy = org.copy()
copy.reverse()

if(org==copy):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
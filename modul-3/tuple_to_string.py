"""Write a Python program to convert a tuple to a string."""

a=('h','e','l','l','o')
print(type(a))
str=''.join(a)
print(str)
print(type(str))

#--------len of tuple------------
"""Write a Python program to find the length of a tuple. """ 

print(len(a))

#----------list to tuple=-----------
"""Write a Python program to convert a list to a tuple"""

lts=[5,10,15,20,25,30,35,40,5,10,-5,-10,-15]

tup_list=tuple(lts)
print(tup_list)

#---------reverce tuple-------
"""Write a Python program to reverse a tuple. """ 

reverse_tuple=tuple(reversed(a))
print(reverse_tuple)


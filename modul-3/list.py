a=[5,10,15,20,25,30,35,40,5,10,-5,-10,-15]
print(a)
print(len(a))

#--------reverse list-----
"""What is List? How will you reverse a list? """ 

a.reverse()
print(f'reverse list ', a)

#---------remove list--------
"""How will you remove last object from a list?  
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?  """


list1=[2, 33, 222, 14, 25]
print(list1)
list1.remove(list1[-1])
print(list1)

#-----------large and small list----------
"""Write a Python function to get the largest number, smallest num and sum 
of all from a list.  """


print(min(a))
print(max(a))
print(sum(a))

#---------compare two lists-----------
"""How will you compare two lists?  """

b=[45,5,36,12,2]
print(set(a) & set(b))

#---------remove duplicate---------
"""Write a Python program to remove duplicates from a list.  """

print(list(set(a)))
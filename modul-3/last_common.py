"""Write a Python function that takes two lists and returns true if they have 
at least one common member.  """


list1=[1,2,3,4,5,6]
list2=[5,6,7,8,9]
for x in list1:
    for y in list2:
        if x==y:
            print("true...")
        else:
            print("false...")
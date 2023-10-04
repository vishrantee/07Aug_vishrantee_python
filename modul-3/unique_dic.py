"""Write a Python program to print all unique values in a dictionary.  """

lts=[{"id":1,"name":"xyz"},{"id":2,"name":"abc",},{"id":1,"name":"aaa",}]
uvalue = set( val for dic in lts for val in dic.values())
print(uvalue)
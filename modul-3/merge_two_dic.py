"""Write a Python script to merge two Python dictionaries  """

std={"id":1,"name":"xyz","age":29}
stcity={"city":"rajkot"}
stud=std.copy()
stud.update(stcity)
print(stud)
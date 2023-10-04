"""Write a Python program to check multiple keys exists in a dictionary  """
std={"id":1,"name":"xyz","age":29}
print(std)
print(std.keys()>={"id","name"})
print(std.keys()>={"id","age"})
print(std.keys()>={"id","1"})
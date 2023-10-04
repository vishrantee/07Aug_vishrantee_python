"""Write a Python script to check if a given key already exists in a 
dictionary."""  


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(i):
  if i in d:
      print('Key is in the dictionary')
  else:
      print('Key is not in the dictionary')
key(5)
key(9)
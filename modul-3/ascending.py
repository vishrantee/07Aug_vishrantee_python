"""Write a Python script to sort (ascending and descending) a dictionary by value.  """


dic={'b':2,'a':1,'d':4,'c':3}
sort_dic=sorted([(value,key)for(key, value) in dic.items()])
print(sort_dic)
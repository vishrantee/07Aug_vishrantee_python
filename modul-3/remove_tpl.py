"""Write a Python program to remove an empty tuple(s) from a list of tuples.  """

tpl=[(),('aaa'),(),('1','2'),(),('3','4'),(),('5','6')]
tpl=[t for t in tpl if t]
print(tpl)
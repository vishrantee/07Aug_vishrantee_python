"""Write a Python program to replace last value of tuples in a list. """ 

lts=[('10','20','30'),('40','50','60'),('70','80','90')]
print([t[:-1] + (100,) for t in lts])
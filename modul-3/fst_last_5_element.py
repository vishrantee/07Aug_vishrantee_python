"""Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30."""  



l=list()
for l in range(1,30):
    l.append(l**2)
    print(l[:5])
    print(l[-5:])

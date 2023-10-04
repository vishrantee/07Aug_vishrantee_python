"""Write a Python program to find the highest 3 values in a dictionary  """

from collections import Counter
d={'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
k=Counter(d)
high=k.most_common(3)
for i in high:
    print(i[0]," :",i[1]," ")
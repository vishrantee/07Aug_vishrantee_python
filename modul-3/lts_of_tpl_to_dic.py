"""Write a Python program to convert a list of tuples into a dictionary. """

lts=[("id",1),("name","xyz"),("age",29)]
dec={}
for key,val in lts:
    dec.setdefault(key,val)
    print(dec)

print(dict(lts))
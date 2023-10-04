"""Write a Python program to map two lists into a dictionary """

key=["id","name","city"]
st1=[1,"aaa","rajkot"]
st2=[2,"xyz","surat"]
print(dict(zip(key,st1)))
print(dict(zip(key,st2)))
"""Write a Python program to check whether a list contains a sub list  """


def getdata(l,s):
    sublist=False
    if s==[]:
        sublist=True
    elif s==l:
        sublist=True
    elif len(s)>len(l):
        sublist=False
    else:
        for i in range(len(l)):
            if l[i]==s[0]:
                n =1
                while(n<len(s))and (l[i+n]==s[n]):
                    n+=1
                if n==len(s):
                    sublist=True

    return sublist
a=['2','4','3','5','7']
b=['4','3']
c=['3','7']
print(getdata(a,b))
print(getdata(a,c))
"""a=input("Enetr value of a :")
b=input("Enetr value of b :")
x=b[:2]+a[2:]
y=a[:2]+b[2:]
print(x , y)"""

def getdata(a,b):
    x=b[:2]+a[2:]
    y=a[:2]+b[2:]
    print(x+'  '+y)

print(getdata('abc','xyz'))
print(getdata('123','789'))
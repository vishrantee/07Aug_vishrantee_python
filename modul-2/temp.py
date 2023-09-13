a=int(input("Enetr value of a :"))
b=int(input("Enetr value of b :"))

#------using temp------


"""temp=a
a=b
b=temp"""

#--------using  tuple--------

a,b=b,a

print("a after swapping :",a)
print("b after swapping :",b)
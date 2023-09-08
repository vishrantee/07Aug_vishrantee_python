n1=int(input("Enter fst no: "))
n2=int(input("Enter snd no: "))
n3=int(input("Enter trd no: "))
sum=(n1+n2+n3)
if (n1==n2) or (n2==n3) or (n1==n3) :
    print("0")
else:
    print("your sum is :",sum)


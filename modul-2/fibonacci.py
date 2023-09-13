num=int(input("Enter your fibonacci sequence: "))
n1,n2=0,1
count=0
if num<=0:
    print("Enter positive number:")
else:
    while count<num:
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
        count+=1
        
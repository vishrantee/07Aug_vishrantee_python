num=int(input("Enter your number :"))
n=1
if num <=0 :
    print("Enter positive number ")
else:
    for i in range(1,num+1):
        n=n*i
        print(n)
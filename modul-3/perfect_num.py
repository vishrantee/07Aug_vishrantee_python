"""Write a Python function to check whether a number is perfect or not.  """

num = int(input("Enter the Number :"))
div = [1]
for i in range(2, num):
	if (num % i)==0:
		div.append(i)
a=sum(div)
print(a)
if a==num:
	print("This is perfect number ")
else:
	print("not a perfect number ")
"""str=input("Enter the String :")
if len(str) % 4 == 0:
   print(''.join(reversed(str)))
else:
	print(str)"""

def getdata(str):
    if len(str) % 4 == 0:
         print(''.join(reversed(str)))
    else:
	    print(str)
          
print(getdata('hello python'))
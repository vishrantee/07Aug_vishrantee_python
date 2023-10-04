"""Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings."""  


str=input("Enter your string :")
if len(str)>2:
    if str[0]==str[-1]:
        print(str)
    else:
        print(" first and last character are not same from a given string ")

else:
    print("Enter a string in more character")


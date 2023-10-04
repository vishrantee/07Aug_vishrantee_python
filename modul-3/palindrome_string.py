"""Write a Python function that checks whether a passed string is palindrome or not  """

str=input("Enter your string :")
if (str==str[::-1]):
    print("this string is palindrome")

else:
    print("this string is not palindrome")

    

def string(str):
    if (str==str[::-1]):
        print("this string is palindrome")

    else:
        print("this string is not palindrome")

string("helooleh")
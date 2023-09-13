def getdata(str):
    if len(str) < 2:
       print("instead of the empty string")
    else:
        print(str[0:2] + str[-2:])

print(getdata('hello python'))
print(getdata('H'))

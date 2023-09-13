"""str = input("Enter your string :")
if len(str)>2:
    if str[-3:]!= 'ing':
        str+='ing'
        print(str)
    elif str[-3:]== 'ing':
        str += 'ly'
        print(str)
else:
    print(str)"""

def getdata(str):
    str1 = len(str)

    if (str1)>2:
        if str[-3:]!= 'ing':
            str+='ing'
            print(str)
        elif str[-3:]== 'ing':
            str += 'ly'
            print(str)
    else:
        print(str)
getdata('ab')
getdata('abc')
getdata('string')

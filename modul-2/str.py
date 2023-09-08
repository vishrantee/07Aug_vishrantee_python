str=(input("Enter your str :"))

#-------length--------

print(len(str))

#------character frequency--------

dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#------occurrences-------

substr=(input("Enter your substring :"))
ocr=str.count(substr)
print(ocr)

#--------count each word-----------


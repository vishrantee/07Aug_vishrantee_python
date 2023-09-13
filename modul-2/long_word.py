str = input("Enter you string : ")
lstr = 0

for i in str.split():
    if len(i) > lstr:
        lstr = len(i)
        longstr = i

print(f"The longest word is {longstr} with length", len(longstr))
def getdata(str):
    counts = dict()
    words = str.split()

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts

print(getdata('hello , everyone how are you? , hello'))
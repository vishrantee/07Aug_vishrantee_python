p =input("Enter your para:")
pnot= p.find("not")
p_poor = p.find("poor")
print(pnot)
print(p_poor)
if pnot>p_poor:
    i=p.replace("not", "poor")
    i=p.replace("poor", "good")
    print(i)
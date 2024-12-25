n=input("Enter a number in Hexadecimal : ")
num=0
for x in range(1,len(n)+1):
    i=n[-x]
    if i =="A":
        d=10
    elif i == "B":
        d=11
    elif i == "C":
        d=12
    elif i == "D":
        d=13
    elif i == "E":
        d=14
    elif i == "F":
        d=15
    else:
        d= int(i)
    num+=d*(16**(x-1))
print("(%s)%c%c = (%d)%c%c"%(n,chr(0x2081),chr(0x2086), num,chr(0x2081),chr(0x2080)))

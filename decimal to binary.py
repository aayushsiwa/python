n=x=int(input("Enter the number in decimal:"))
b=0
pl=0
while n>0:
        d=n%2
        n//=2
        b+=d*(10**pl)
        pl+=1
print("(%d)%c%c=(%s)%c"%((x,chr(0x2081),chr(0x2080), b,chr(0x2082))))

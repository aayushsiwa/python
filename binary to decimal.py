'''WAP to accept a number in binary system and
represent the same in decimal system'''
n=x=int(input("Enter the number in binary:"))
b=0
pl=0
while n>0:
        d=n%10
        n//=10
        b+=d*(2**pl)
        pl+=1
print("(%d)%c = (%d)%c%c"%(x,chr(0x2082),b,chr(0x2081),chr(0x2080)))

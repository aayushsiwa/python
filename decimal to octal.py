'''WAP to accept a number in decimal system
and represent the same in Octal system.'''
n=x=int(input("Enter the number in decimal:"))
b=0
pl=0
while n>0:
        d=n%8
        n//=8
        b+=d*(10**pl)
        pl+=1
print("The (%d)%c%c  = (%d)%c"%(x,chr(0x2081),chr(0x2080),b,chr(0x2088)))

n=x=int(input('Enter the number in octal:'))
b=0
pl=0
while n>0:
    d=n%10
    n//=10
    b+=d*(8**pl)
    pl+=1
print('(%d)%c=(%d)%c%c'%(x,chr(0x2088),b,chr(0x2081),chr(0x2080)))

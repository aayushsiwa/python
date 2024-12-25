n=int(input('enter a number:'))
x=int(input('enter the first term:'))
s=0
for i in range(0,n):
    if i%2==0:
        s+=x**i
    else:
        s-=x**i

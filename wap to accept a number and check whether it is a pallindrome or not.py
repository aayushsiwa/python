#wap to accept a number and check whether it is a pallindrome or not
x=int(input('enter the number'))
n=x
rev=0
while x>0:
    rev=rev*10+x%10
    x//=10
if rev==n:
    print ("The number is a pallindrome")
else:
    print ("The number is not a Pallindrome")

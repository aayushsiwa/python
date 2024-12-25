#wap accept a 3 digit number and show it is a pallindrome or not
rev=0
n=int(input('enter the number'))
x=n
while x>0:
    rev=rev*10+x%10
    x//=10
if rev==n:
    print('it is a pallindrome')
else:
    print('it is not a pallindrome')    

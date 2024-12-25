a=input('enter the first digit of the number ')
b=input('enter the second digit of the number')
c=input('enter the third digit of the number')
n=100*a+10*b+c
m=100*c+10*b+a
if n==m:
	print('the number is a pallindrome')
else:
	print('the number is not a pallindrome')

#Wap to accept year as input and check whether it is a leap year or not
year=int(input('Enter the year:'))
l=year%4
if l==0:
    print('Its a leap year')
else:
    print('Its not a leap year')

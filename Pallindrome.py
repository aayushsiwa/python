#to check whether the number is a palindrome or not
n=int(input("Enter the number:"))
x=n
rev=0
while x>0:
    rev=rev*10+x%10
    x//=10
if rev==n:
    print ("The number is a pallindrome")
else:
    print ("The number is not a Pallindrome")

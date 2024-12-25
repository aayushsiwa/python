pallin=[]
lst=[]
prime=[]
palprime=[]
q=int(input('enter the numbers of imputs:'))
for i in range(q):
    n=int(input("Enter the number:"))
    lst.append(n)
    x=n
    rev=0
    while x>0:
        rev=rev*10+x%10
        x//=10
    for i in range(len(lst)):
        p=0
        for j in range(1,lst[i]):
            if lst[i]%j==0:
                p+=1
        if p==1:
            prime.append(lst[i])
            print ("The number is a prime")
            break
        else:
            print('The number is not a prime')
    if rev==n:
        print ("The number is a pallindrome")
        pallin.append(n)
    else:
        print ("The number is not a Pallindrome")
x=len(prime)
q=len(pallin)
print('Prime numbers are ',prime)
print('Pallindromes are',pallin)
print('There are %d prime numbers'%x)
print('There are %d pallindromes'%q)

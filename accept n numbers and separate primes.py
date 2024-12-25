x=int(input("Enter the numbers of numbers you want to give as input:-"))
lst = []
prime = []
for i in range(x):
    n=int(input("enter the number: "))
    lst.append(n)
for i in range(len(lst)):
    q=0
    for j in range(1, lst[i]):
        if lst[i]%j == 0:
            q += 1
    if q == 1:
        prime.append(lst[i])
print('The prime numbers are:')
for i in range(len(prime)):
    print(prime[i])

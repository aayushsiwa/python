x=int(input("Enter the number of integers you want you accept:-"))
lst = []
Pallin = []

for i in range(x):
    n = int(input("enter the number: "))
    lst.append(n)

for i in range(len(lst)):
    rev = 0
    m = lst[i]
    while m > 0:
        rev = rev*10 + m%10
        m = m//10
    if rev == lst[i]:
        Pallin.append(lst[i])
        
k = sum(Pallin)
print("Sum of the palindromes that you have given in the list is:",k)

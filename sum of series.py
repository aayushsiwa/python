x=int(input("Enter a number:"))
n=int(input("Enter the number of terms:"))
s=0
for i in range(n+1):
    s=s+x**i
print("The sum of the given series is",s)

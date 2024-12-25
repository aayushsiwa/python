n=int(input("Enter the no. of objects:-"))
r=int(input("Enter the no. of ways:-"))
import math
q=math.factorial(n)
w=math.factorial(n-r)
npr=float(q/w)
print("npr is",npr)

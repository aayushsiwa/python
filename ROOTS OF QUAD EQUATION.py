# WAP to find roots of a quadratic equation
a=int(input("coeff. of x^2:"))
b=int(input("coeff. of x:"))
c=int(input("coeff. of x^0:"))
d=b**2-4*a*c
x=-b+d**0.5
y=-b-d**0.5
if d==0:
    print("the roots are",x,x)
elif d<0:
    print("the roots are not real")
else:
    print("if x and y are roots of the quadratic equation",x,y)

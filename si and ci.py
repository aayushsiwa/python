p=int(input("enter the principal:"))
r=int(input("enter the rate of interest:"))
t=int(input("enter the time:"))
print("the simple interest is",(p*r*t)/100)
asi=p+(p*r*t)
print("the amount for simple interest is",asi)
aci=p+(p*((1+r/100)**t-1))
print("the amount for compound interest is",aci)
print("the difference in amount of compound and simple interest is",aci-asi)

n=int(input("Enter the number of inputs: "))
l=list()
for i in range(n):
        print("Enter the %dth element:- "%(i+1),end="")
        l.append(int(input()))
ctr=0
for i in l:
        if i%2==0:
            ctr+=1
print("The percentage of even numbers is %f"%(ctr*100/n))

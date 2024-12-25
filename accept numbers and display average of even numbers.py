l=list()
for i in range(10):
        print("Enter the %dth element:- "%(i+1),end="")
        l.append(int(input()))
ctr=s=0
for i in l:
        if i%2==0:
            ctr+=1
            s+=i
print("The average of even numbers is %f"%(s/ctr))

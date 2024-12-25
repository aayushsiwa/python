l=list()
for i in range(10):
        print("Enter the %dth element"%(i+1))
        l.append(int(input()))
ctr=0
for i in l:
        if i%2==0:
            ctr+=1
print("There are %d even numbers"%ctr)

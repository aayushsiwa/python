x=input("Enter the word:-")
lst=[]
m=len(x)
for k in x:
    lst.append(k)
for j in lst:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        for l in range(-1*(m+2),m+2):
            lst[l]=lst[l-1]

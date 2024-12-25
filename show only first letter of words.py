x=int(input("Enter the number of words:-"))
lst=[]
o=[]
for i in range(0,x):
    a=input('Enter the word:-')
    lst.append(a[0])
for k in range(0,x):
    o.append(lst[k].capitalize())
m=o[0]
for j in range(1,x):
    m+=' '
    m+=(o[j])
print(m)

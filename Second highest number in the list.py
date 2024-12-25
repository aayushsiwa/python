n=int(input('Enter the number of elements of the list:-'))
lst=[]
for i in range(n):
    x=int(input('Enter the element #%d:-'%(i+1)))
    lst.append(x)
max1=max(lst)
i=lst.index(max1)
lst[i]=min(lst)
for i in lst:
    if i==max1:
        j=lst.index(i)
        lst[j]=min(lst)
max2=max(lst)
print('The second maximum value in the list is %d'%max2)

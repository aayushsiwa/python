lst=[]
binary=input('Enter the binary number:')
for i in binary:
    lst.append(i)
decimal=[]
a=0
binary=lst.reverse()
for i in range(0,len(lst)):
    a=int(lst[i])
    decimal[i]=(2**a)
print(sum(decimal))

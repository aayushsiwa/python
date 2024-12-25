#wap write a prog to take number of books available as n and no.of books to be plied on the rack out of it as r.Now,find out the number of ways we can arrange the rack.
n=int(input("Enter the total number of books :"))
r=int(input("Enter the number of books to be arranged :"))
f=1
for i in range(1,n+1):
    f=f*i
f1=1
for i in range(1,n-r+1):
    f1=f1*i
npr=f/f1
print("The number of ways in which books can be arranged is",npr)


    
    

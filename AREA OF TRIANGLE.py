a=int(input("length of side 1:"))
b=int(input("length of side 2:"))
c=int(input("length of side 3:"))
p=a+b+c
print("perimeter of triangle",p)
sp=int(p/2)
a=(sp*(sp-a)*(sp-b)*(sp-c))**0.5
print("area of triangle",a)
print('happy ')
print('hello')

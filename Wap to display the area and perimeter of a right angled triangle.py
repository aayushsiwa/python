#wap to display the area and perimeter of a right angled triangle
p=int(input('enter the length of the perpendicular of the triangle:'))
b=int(input('enter the length of the base of the traingle:'))
h=(p**2 + b**2)**0.5
perimeter=p+b+h
print('perimeter of the traingle is',perimeter)
area=0.5*p*b
print('area of the triangle is',area)

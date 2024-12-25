r=int(input("enter the radius of the base of the cone:"))
h=int(input("enter the hieght of the cone:"))
l=int(input("enter the slant hieght:"))
if l=='not given':
    l=((h**2)+(r**2))**(0.5)
elif h=='not given':
    h=((l**2)-(r**2))**(0.5)
csa=3.14*r*l
print("curved surface area of the cone is ",csa)
tsa=3.14*r*(l+r)
print("total surface area of the cone is",tsa)
v=0.33*3.14*r**2*h
print("the volume of cone is",v)

r=int(input("radius of cylinder:"))
h=int(input("hieght of cylinder:"))
csa=2*3.14*r*h
tsa=2*3.14*r*(r+h)
v=3.14*(r**2)*h
print("CSA of cylinder",csa)
print("TSA of cylinder",tsa)
print("VOLUME of cylinder",v)

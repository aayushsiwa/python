import math
x=int(input("Enter the angle:-"))
z=str(input("Enter the unit of angle(rad for radians and deg for degrees):-"))
y=str(input("Enter the function you want to perform on the angle(cos-cosine;sin-sine;tan-tangent;sec-secant;cosec-cosecant;cot-cotangent):-"))
if z=='rad':
    if y=='cos':
        print('Cosine of the required angle is:',math.cos(x))
    elif y=='sin':
        print('Sine of the required angle is:',math.sin(x))
    elif y=='tan':
        print('Tangent of the required angle is:',math.tan(x))
    elif y=='sec':
        print('Secant of the required angle is:',(math.cos(x))**(-1))
    elif y=='cosec':
        print('Cosecant of the required angle is:',(math.sin(x))**(-1))
    elif y=='cot':
        print('Cotangent of the required angle is:',(math.tan(x))**(-1))
    else:
        print('Error...please try again')
elif z=='deg':
    x=float(math.degrees(x))
    if y=='cos':
        print('Cosine of the required angle is:',math.cos(x))
    elif y=='sin':
        print('Sine of the required angle is:',math.sin(x))
    elif y=='tan':
        print('Tangent of the required angle is:',math.tan(x))
    elif y=='sec':
        print('Secant of the required angle is:',(math.cos(x))**(-1))
    elif y=='cosec':
        print('Cosecant of the required angle is:',(math.sin(x))**(-1))
    elif y=='cot':
        print('Cotangent of the required angle is:',(math.tan(x))**(-1))
    else:
        print('Error...please try again')

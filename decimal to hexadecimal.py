'''WAP to accept a number in decimal and display
the equivalent hexadecimal...'''
x=d_num = int(input("Enter the number in decimal form: "))
h_num = ""
dig=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while x > 0:
    d = x%16
    x //= 16
    h_num = dig[d]+h_num
print("(%d)%c%c = (%s)%c%c"%(d_num,chr(0x2081),chr(0x2080), h_num,chr(0x2081),chr(0x2086)))

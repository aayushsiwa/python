#Program to convert hexadecimal to octal
n=(input("Enter a number in Hexadecimal : "))
num=str()
dict={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'10','9':'11','A':'12','B':'13','C':'14','D':'15','E':'16','F':'17'}
for i in n:    
    for j in dict:
        num+=dict[i]    
        break
print("(%s)%c%c=(%s)%c"%((n,chr(0x2081),chr(0x2086),num,chr(0x2088))))

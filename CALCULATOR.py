a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
s=(a+b)
f=(a-b)
d=(a/b)
p=(a*b)
c=((a/b)*100)
do=str(input("enter the operation you want to do i.e., add-s,diff-f,divide-d,multiply-p,percentage-c:"))
if do=='s':
    print("answer is:",s)
elif do=='f':
    print("answer is:",f)
elif do=='d':
    print("answer is:",d)
elif do=='p':
    print("answer is:",p)
elif do=='c':
    print("answer is:",c)
else:
    print("error...try again")

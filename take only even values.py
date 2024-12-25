num=int(input("Enter the number:-"))
ctr=0
while num>0:
    ctr+=1
    s=num%10
    num//=10
    if ctr%2==0:
      print(s)
      

ctr=0
while ctr>=0:
    num=int(input("Enter the number:-"))
    ctr+=1
    s=num%10
    num//=10
    if ctr%2==0:
      print(s)

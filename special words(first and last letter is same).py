x=(input("Enter the word:-"))
lst=[]
m=len(x)
for i in x:
      lst.append(i)
if lst[0]==lst[m-1]:
    print("THIS WORD IS A SPECIAL WORD")
else:
    print("THIS WORD IS NOT A SPECIAL WORD")

              

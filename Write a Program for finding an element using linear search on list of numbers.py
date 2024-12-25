lst = [4, 2, 8, 9, 3, 7]
x = int(input("Enter number to search: "))
found = False
for i in range(len(lst)):
    if(lst[i] == x):
        found = True
        print("%d found at %dth position"%(x,i))
        break
if(found == False):
    print("%d is not in list"%x)

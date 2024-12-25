#wap to accept 10 numbers and display their sum,average,minimum,maximum
l=[]
for i in range(0,10):
    x=int(input('enter the number'))
    l.append(x)
print(max(l),min(l),sum(l),sum(l)/len(l))

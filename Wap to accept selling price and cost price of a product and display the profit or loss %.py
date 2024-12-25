#wap to accept selling price and cost price of a product and display the profit or loss %
cp=int(input('Enter the cost price i.e.,the price at which it was bought:'))
sp=int(input('Enter the selling price i.e,the price at which it was sold:'))
profit=((sp-cp)/cp)*100
loss=((cp-sp)/cp)*100
if sp>cp:
    print('There is a profit of',profit,'%')
elif cp>sp:
    print('There is a loss of',loss,'%')
elif cp==sp:
    print('There is no profit and no loss')

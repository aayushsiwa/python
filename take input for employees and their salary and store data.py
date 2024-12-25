n=int(input("Enter the number of employees:- "))
dic=dict()
for i in range (1,n+1):
    print("Enter name of employee ",i,":- ",end='')
    name=input()
    print("Enter salary of ", name,":- ",end='')
    salary= int(input())
    dic[i]={"Employee name":name,"Salary":salary}
print("The Records are")
print("Employee name-Salary")
for i in dic:
    print(dic[i]['Employee name'],'-',dic[i]['Salary'])

def changeRecord():
    import pickle
    import os
    import sys
    #reading and showing the original file
    file = open("e:\\files\\student.dat","rb")
    lst = pickle.load(file)
    file.close()
    print("+--------+-----------------+")
    print("| Roll No|  Name of Student|")
    print("+--------+-----------------+")
    for i in lst:
        print("|",str.ljust(i['roll'],6),'|',str.rjust(i['name'],15),"|",end="\n")
        print("+--------+-----------------+")
    print("No More Data Selected")

    #to change the target record element and the loaded list
    ele=input("Enter the roll number of the record to be Updated:-")
    lt=[]
    flg=False
    for i in lst:
        if i['roll']==ele:
            flg=True
            print("Roll number is",i['roll'])
            x=input("Enter 'y'/'Y' to change:-")
            if x=='y' or x=='Y':
                i['roll']=int(input("Enter the new Roll number:"))
            print("Name is",i['name'])
            x=input("Enter 'y'/'Y' to change:-")
            if x=='y' or x=='Y':
                i['name']=input("Enter the new name:")      
            lt.append(i)
        else:
            lt.append(i)
        
    if flg:
        print("Record will be Updated")
    else:
        sys.stderr.write("No such data found to change")
        return
    

    #to dump the updated list into a new(duplicate) file
    file = open("e:\\files\\student1.dat","wb")
    pickle.dump(lt,file)
    file.close()

    #removing the original file
    os.remove("e:\\files\\student.dat")
    #renaming the new file with the name of original file
    os.rename("e:\\files\\student1.dat","e:\\files\\student.dat")

    #showing the updated file
    file = open("e:\\files\\student.dat","rb")
    lst = pickle.load(file)
    file.close()
    print("+--------+-----------------+")
    print("| Roll No|  Name of Student|")
    print("+--------+-----------------+")
    for i in lst:
        print("|",str.ljust(i['roll'],6),'|',str.rjust(i['name'],15),"|",end="\n")
        print("+--------+-----------------+")
    print("No More Data Selected")
changeRecord()

perc=int(input("enter the child's percentage:"))

if perc>100:
    print("error...try again")
elif perc>85:
    print("GRADE-A")
elif perc>70 and perc<=85:
    print("GRADE-B")
elif perc>60 and perc<=70:
    print("GRADE-C")
elif perc>45 and perc<=60:
    print("GRADE-D")
elif perc<=45:
    print("REMARK-FAILED")
if perc>100:
    print("error...try again")
elif perc>33:
    print("REMARK-PASSED and PROMOTED")
else:
    print("REMARK-FAILED")


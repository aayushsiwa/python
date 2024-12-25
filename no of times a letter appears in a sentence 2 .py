st=input("Enter the sentense:")
st=st.lower()
dct=dict()
for letter in range(ord('a'),ord('z')+1):
    freq=0
    for i in st:
        if ord(i)==letter:
            freq+=1
    if freq>0:
        dct[chr(letter)]=freq
print("Frequency Table\nLetter - frequency")
for i in dct:
    print(i,"-",dct[i])

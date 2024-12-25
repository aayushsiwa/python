st=str(input("Enter the sentence:"))
st=st.lower()
dct=dict()
for letter in "abcdefghijklmnopqrstuvwxyz":
    freq=0
    for i in st:
        if i==letter:
            freq+=1
    if freq>0:
        dct[letter]=freq
print("Frequency Table\nLetter - Frequency")
for i in dct:
    print('|',i,'|',"--->",'|',dct[i],'|')

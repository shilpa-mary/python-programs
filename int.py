len=int(input("How Many nos do you wants to save?"))
inputvaluelist=[]
for n in range(0,len):
    inputvalue=int(input("enter a volue"))
    if inputvalue>=100:
        inputvaluelist.append("OVER")
    else:
        inputvaluelist.append(inputvalue)
print(inputvaluelist)
        

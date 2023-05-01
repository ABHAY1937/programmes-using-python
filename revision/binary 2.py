lst=[1,3,5,89,7,56,4,5,1,57,22]
flag=0
element=int(input("enter the element"))
upp=len(lst)-1
low=0
for i in range(low,upp+1):
    mid=(low+upp)//2
    if(element>lst[mid]):
        upp=mid-1
    elif(element<lst[mid]):
        low=mid+1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found",mid)
else:
    print("OOPPS!!!!")
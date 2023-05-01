num=[2,3,5,7,9]
element=int(input("enter the number"))
flag=0
upp=len(num)-1
low=0

for i in range(low,upp+1):
    mid = (low + upp) // 2
    if(element<num[mid]):
       upp=mid+1
    elif(element>num[mid]):
        low=mid-1
    elif(element==num[mid]):

        flag=1
        break
if(flag>0):
    print("number found",mid)
else:
    print("element not found!!!")
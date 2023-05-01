element=int(input('Enter the values'))
lst=[1,12,4,47,8,9,55,6,4,5,1,5,2,54,1,5,2,2,5,2,5,5,58,54,5,8,54,25,2,5,5]
print(lst)
flag=0
#sorting in ascending order
lst.sort()
print(len(lst))
upp=len(lst)-1
low=0

#mid =

for i in range(low,upp+1):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found",mid) #mid is used for finding the position

else:
    print('not found')
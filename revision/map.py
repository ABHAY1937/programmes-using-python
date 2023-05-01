lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(map(lambda num:num**2,lst))
print(lst1)

lst2=list(filter(lambda num:num%2==0 ,lst))
print(lst2)

lst3=list(filter(lambda num:num%2!=0 ,lst))
print(lst3)

lst4=list(filter(lambda num:num%2==0,lst))
lst5=list(map(lambda num:num**3,lst4))
print(lst5)

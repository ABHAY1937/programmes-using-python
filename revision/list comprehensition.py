lst=[i for i in range(1,31) if i%2==0]
print(lst)

f=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,30)]
print(f)
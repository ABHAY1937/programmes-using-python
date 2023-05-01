name=['sabu','babu','chakku','tappu']
animal=['cow','goat','cat','dog']
number=[1,2,3,4]
z=zip(name,animal,number)
for name,animal,number in z:
    print("%s the %s is %s"%(name,animal,number))
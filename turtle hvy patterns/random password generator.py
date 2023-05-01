import random
passlen=int(input("enter the length of the password"))
s='abcdefghijklmnopqrstuvwxyz12345678903256415845415ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()?><:0'
P="".join(random.sample(s,passlen))
print(P)
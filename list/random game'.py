import random

flowers=["rose","jasmine","lilly","lotus","jamanthi"]
print("List=",flowers)
selection=str(input("enter your selection"))
comp_guess=random.randrange(0,5)
guess=flowers[comp_guess]
if(selection==guess):
    print("you win")
else:
    print("you failed")
print("computer selection =",guess)
print("your selection",selection)
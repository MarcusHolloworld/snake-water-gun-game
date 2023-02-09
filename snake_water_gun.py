import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("computer choose a option for snake(s),water(w) and gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input(f"your turn: choose a option for snake(s),water(w) and gun(g)?\n")
print(f"computer choose {comp}")
print(f"you choose {you}")
f=gamewin(comp,you)
if f==True:
    print("you win:")
elif f==False:
    print("you losh:")
else:
    print("the game is tie:")

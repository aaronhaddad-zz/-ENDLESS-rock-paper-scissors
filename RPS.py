import random

winner=""

print("We are gonna play rock, paper, scissors!")
options=["rock","paper","scissors"]
print("The options are: ",end="")
for i in range(3): print(options[i],sep=" ",end=" ")
comp=""
usr=""
print()
print("U start!")

while winner=="":
    compPick=random.randrange(0,3,1)
    print(options[compPick])
    usr=input()
    if usr=="rock" and options[compPick]=="paper":
        print("I win!")
        winner="machine"
    break
    if usr=="rock" and options[compPick]=="scissors":
        print("U win!")
        winner="user"
    break
    if usr=="paper" and options[compPick]=="scissors":
        print("I win")
        winner="machine"
    break
    if options[compPick]=="rock" and usr=="paper":
        print("U win")
        winner="user"
    break
    if options[compPick]=="rock" and usr=="scissors":
        print("I win")
        winner="machine"
    break
    if options[compPick]=="paper" and usr=="scissors":
        print("U win!")
        winner="user"
    break


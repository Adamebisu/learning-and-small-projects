import random

dash = "-"
rand1 = str(random.randint(0,10000))
rand2 = str(random.randint(0,10000))
print("number 1 is", rand1)
print("number 2 is ", rand2)

if int(rand1) > int(rand2):
    biggest = rand1
elif int(rand2) > int(rand1):
    biggest = rand2
elif int(rand1) == int(rand2):
    biggest = rand1
print("biggest is", biggest)
dashlen = len(biggest) * dash + "--"
print(dashlen)
print(len(dashlen))
ralign1 = len(dashlen)
print("ralign 1:", ralign1)
ralign2 = len(dashlen) - 1
print("ralign 2:", ralign2)

print(rand1.rjust(ralign1), "\n", "+", rand2.rjust(ralign2), "\n", dashlen, sep="")

#my_text = 'shift me.'
#print(my_text.rjust(1))
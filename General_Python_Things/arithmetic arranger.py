
list = ["30 + 31", "911 - 15"]
formatted = []
formattedsum = []
formatted1 = 0
formatted2 = 0
formatted3 = 0
formatted4 = 0
#error check: problem count
if len(list) > 5:
    print("Too many problems")
    exit()
for i in list:
    counter = 1
    dash = "-"
    biggest = 0
    splitted = i.split()
    #print(splitted)
    #print(splitted[1])
    #print(type(splitted[1]))
    #print(splitted[0])
    #print(splitted[2])
    #error check: operator
    if splitted[1] == '/':
        print("Error: Operator must be '+' or '-'.")
        break
    elif splitted[1] == '*':
        print("Error: Operator must be '+' or '-'.")
        break
    #error check: numbers are digits
    try:
        intnum1 = int(splitted[0])
        intnum2 = int(splitted[2])
        sum = intnum1+intnum2
        #print("1 and 2 are", intnum1, intnum2, "sum is", sum)
    except:
        print("Error: Numbers must only contain digits.")
    #error check: number length
    if len(splitted[0]) > 4:
        print("Error: Numbers cannot be more than four digits.")
    elif len(splitted[2]) > 4:
        print("Error: Numbers cannot be more than four digits.")
    if intnum1 > intnum2:
        biggest = intnum1
    elif intnum1 < intnum2:
        biggest = intnum2
    elif intnum1 == intnum2:
        biggest = intnum1
    #print("biggest is", biggest)
    dashlen = len(str(biggest)) * dash + "--"
    #print(dashlen)
    #print(len(dashlen))
    ralign1 = len(dashlen)
    #print("ralign 1:", ralign1)
    ralign2 = len(dashlen) - 1
    #print("ralign 2:", ralign2)
    if counter == 1:
        formatted1 = print(splitted[0].rjust(ralign1), "\n", splitted[1], splitted[2].rjust(ralign2), "\n", dashlen, sep="")
    if counter == 2:
        formatted2 = print(splitted[0].rjust(ralign1), "\n", splitted[1], splitted[2].rjust(ralign2), "\n", dashlen, sep="")
    if counter == 3:
        formatted3 = print(splitted[0].rjust(ralign1), "\n", splitted[1], splitted[2].rjust(ralign2), "\n", dashlen, sep="")
    if counter == 4:
        formatted4 = print(splitted[0].rjust(ralign1), "\n", splitted[1], splitted[2].rjust(ralign2), "\n", dashlen, sep="")
    counter += 1
    #print(splitted[0].rjust(ralign1), "\n", splitted[1], splitted[2].rjust(ralign2), "\n", dashlen, sep="")

formatted1

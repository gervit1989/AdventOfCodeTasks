sum = 0
sum2 = 0
try:
    lines1 = []
    lines2 = []
    with open('data.txt','r') as in_file:
        for line in in_file:
            list = line.strip().split()
            lines1.append(list[0])
            lines2.append(list[1])
    if len(lines1) == len(lines2) and len(lines1) > 0:
        lines1.sort()
        lines2.sort()
    print(lines1)
    print(lines2)
    for i in range(len(lines1)):
        val = int(lines1[i])
        length = abs(val - int(lines2[i]))
        #print(length)
        sum += length
        sum2 += val * lines2.count(lines1[i])

except FileNotFoundError:
    print("correct exit on nonfound")
finally:
    print("End:= " + str(sum) +", "+str(sum2))


#2970687 23963899
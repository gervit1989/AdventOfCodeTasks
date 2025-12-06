def checkstr(list):
    errlst = []
    diff1 = 0
    diff = 0
    bWas = 0
    for i in range(1, len(list)):
        diff1 = diff
        val = int(list[i])
        val2 = 0
        try:
            val2 = int(list[i - 1])
        except ValueError:
            val2 = list[i - 1]
            # print(val2)
            val2 = val2[-2:len(val2)]
            val2 = int(val2)
        finally:
            xj = 1
        # print("x="+str(val2))
        diff = val - val2
        if (diff1 * diff < 0):
            bWas = 1
            errlst.append(i)
        else:
            if not (abs(diff) >= 1 and abs(diff) <= 3):
                bWas = 1
                errlst.append(i)
    return errlst


file = open('input.txt', 'r')
lines = file.readlines()
file.close()
# print(lines)
count = 0
for line in lines:
    list = line.strip().split()
    # print(list)
    errlst = checkstr(list)
    n1 = len(errlst)
    if n1 == 0:
        count += 1
    elif n1 >= 1:
        # if n1 >2:
        # continue
        print("\n errs")
        print(list)
        print(errlst)
        for i in range(len(list)):
            var1 = i
            list1 = list[:var1]
            print(var1, list1)
            if i < len(list) - 1:
                list1 += list[var1 + 1:len(list)]
            print(list1)
            if len(list1) == 0:
                continue
            errs = checkstr(list1)
            if len(errs) == 0:
                print(list1)
                count += 1
                print("fix", count)
                break

print(count)


#ans 246 318
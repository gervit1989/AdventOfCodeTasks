
def read_data():
    in_data = []
    with open("in.txt", "r") as fin:
        in_data = list(fin.read().strip())
    return in_data

line = read_data()
print(*line)

pos = 0
id_var = 0
out_data=[]
line1 = [int(line[i]) for i in range(len(line)) if i%2]
line2 = [int(line[i]) for i in range(len(line)) if i%2 ==0]
print(len(line1), len(line2))
print(line1, line2, sep ='\n')
dots = []
digits = []
for elem in line:
    symb = ('.' if pos %2 else str(id_var))
    #print(pos, dots, id_var, digits)
    if pos % 2 == 0:
        id_var += 1
        digits.append(len(out_data))
    else: #if int(elem) > 0:
        dots.append(len(out_data))
    for i in range(int(elem)):
        out_data.append(symb)
    pos+=1
dbg = open("task.dbg", "w")
str_out =''
for elem in out_data:
    symb = elem
    symb = "[" + "{:4s}".format(elem)+"]"
    str_out +=symb
dbg.write(str_out+"\n len: "+str(len(out_data))+"\n")
#print("dots:",dots)
#print(digits)
for i in range(len(line2)-1, 0, -1):
    is_found= False
    j_start = -1
    len_cur = int(line2[i])
    shift2 = digits[i]
    shift1 = 0
    for j in range(len(line1)):
        shift1 = dots[j]
        if int(line1[j]) >= len_cur and shift1 < shift2:
            is_found = True
            j_start = j
            break
    if is_found:
        #dbg.write("shifts: "+str( shift1)+"," +str(shift2)+"\n")
        for k in range(len_cur):
            out_data[shift1 + k] = out_data[shift2+k]
            out_data[shift2 + k] = '.'
        if int(line1[j_start]) == len_cur:
            #print("zzz")
            dbg.write("zzz\n")
            dots[j_start] += len_cur
            line1[j_start] -=len_cur
        else:
            #print("xxx")
            dbg.write("xxx\n")
            dots[j_start] += len_cur
            line1[j_start] -=len_cur
        #print("dbg: ", dots[j_start], line1[j_start])
        #dbg.write("dbg: "+ str(dots[j_start]) +"," +str(line1[j_start])+"\n")
    else:
        print("no place\n")
    # str_out =''
    # for elem in out_data:
    #     str_out +=elem
    # dbg.write(str_out+"\n")
str_out =''
for elem in out_data:
    symb = elem
    symb = "[" + "{:4s}".format(elem)+"]"
    str_out +=symb
dbg.write(str_out+"\n len: "+str(len(out_data))+"\n")
#print(*list("00992111777.44.333....5555.6666.....8888.."))
#out_data = list("0099811188827773336446555566..............")
sum_var = 0
for i in range(len(out_data)):
    if not out_data[i].isdigit():
        continue
    sum_var += i *int(out_data[i])
if sum_var < 8564936405055:
    print("ans: ", sum_var)
dbg.close()
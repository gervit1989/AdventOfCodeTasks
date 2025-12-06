#https://adventofcode.com/2024/day/7/input

def read_data():
    with open('in.txt', 'r') as file:
        indexes = []
        keys = []
        length = 0
        while True:
            line = file.readline().strip()
            if line:
                lst1 = line.split(':')
                lst2 = lst1[1].strip().split(" ")
                indexes.append(lst2)
                keys.append(lst1[0])
                length = (length if length > len(lst2) else len(lst2))
            else:
                break
        print("max len: ", length)
        return [length, keys,indexes]

def gen_oper_vars(leng, avail, map):
    ans = []
    avail_len = len(avail)
    if leng == avail_len and leng ==2:
        ans = avail
    elif leng == avail_len and leng ==3:
        ans.append(avail)
        
    elif leng<avail_len and leng == 2:
        pos_x = 0
        while True:
            ans.append(avail[pos_x:pos_x+2])
            pos_x+=1
            if pos_x + 1 >=avail_len:
                break
    else:
        count_ck = 0
        lst = map[str(leng - 1)]
        for oo in lst:
            for o in avail: ans.append(oo + o)

    print(*ans)
    return ans

#print(gen_oper_vars(2, ['*','+', '|']), sep="\n")


def solution():
    # ввод
    ans1 = read_data()
    max_len = ans1[0]
    keys = ans1[1]
    lines = ans1[2]
    rlines = []
    lines_other= []
    is_out = False
    is_out = True
    out1 = None
    gen_map = {}
    operation_avails=['*','+', '|']
    if is_out:
        out1 = open("task.log", "w")
    for i in range(2, max_len+1):
        print("gen ", i)
        gen_map[str(i)] = gen_oper_vars(i, operation_avails, gen_map)
        # break

    for k in range(len(keys)):
        if not (k == 281):
            continue
        print(k)
        key_var = keys[k]
        data = lines[k]
        if is_out:
            out1.write(str(key_var) + ":" + str(data)+"\n")
        is_found = False
        length = len(data)
        variants = gen_map[str(length)]
        operation_vars_len = len(variants)
        if is_out and 0:
            for pos in range(operation_vars_len):
                out1.write(str(variants[pos]) +"\n")
        count_gr = 0
        count_z = 0
        for pos in range(operation_vars_len):
            cur_op_count = variants[pos].count(operation_avails[0])
            if count_z != cur_op_count:
                count_z =cur_op_count
                count_gr = 0
            if is_out:
                out1.write(str(variants[pos]) +"\n")
            var = data[0]
            for i in range(length-1):
                operation = variants[pos][i]
                str_val = (str(var) + operation + str(data[i+1]))
                if operation == '|':
                    var = str(var) + str(data[i+1])
                elif operation == '*':
                    var = int(var) * int(data[i+1])
                else:
                    var = int(var) + int(data[i+1])
                    #var = eval(str_val)
                if is_out:
                    out1.write(str_val+"= "+str(var)+"\n")
                if int(var) == int(key_var):
                    is_found = True
                    rlines.append([key_var,data])
                    break
                if int(var) >= int(key_var):
                    break
            if is_found:
                break
            if int(var) > int(key_var) and is_out:
                out1.write("key is less var\n")
            if int(var) < int(key_var):
                count_gr +=1
                if is_out:
                    out1.write("key is greater var : " + str(count_gr)+"\n")
            if is_out:
                out1.write("count gre: " + str(count_gr)+"\n")
            if count_gr >= length-1:
                break
        if not is_found:
            lines_other.append([key_var,data])
        #break
    if is_out and out1 is not None:
        out1.close()
    return [rlines,lines_other]

print("Start")
ans = solution()
print("solved")
lines1 = ans[0]
lines2 = ans[1]
sum_var = 0
print(eval("'23'+'45'"))
out_r = open("rights.txt", 'w')
for i in range(len(lines1)):
    sum_var += int(lines1[i][0])
    out_r.write(str(int(lines1[i][0]))+ ": "+str(lines1[i][1])+"\n")
out_r.close()
if sum_var > 553765366338 and sum_var > 2773656637753:
    print("ans: ", sum_var)
out2 = open("errs.txt", 'w')
for i in range(len(lines2)):
    sum_var += int(lines2[i][0])
    out2.write(str(int(lines2[i][0]))+ ": "+str(lines2[i][1])+"\n")
out2.close()
# # 553765366338 is low
# # 2773656637753 is low

from collections import defaultdict


def read_data():
    in_data = []
    with open("in.txt", "r") as fin:
        in_data = list(map(int, fin.readline().strip().split()))
    return in_data
def to_line(map_data):
    str_data1 = ''
    for key1, val1 in map_data.items():
        if val1 == 0:
            continue
        str_data1 += str(key1) + ':' + str(val1) + ', '
    return str_data1

init_line = read_data()
blinks = 75
print(*init_line)
work_line = defaultdict(int)

for elem in init_line:
    if elem in work_line.keys():
        work_line[elem] +=1
    else:
        work_line[elem] = 1
ansf = open("ans.txt",'w')
for varc in range(blinks):
    lst_keys =[]
    for key,val in work_line.items():
        if val == 0:
            continue
        lst_keys.append(key)
    len1 = len(lst_keys)
    print("blink: ", varc, len1)
    new_line = defaultdict(int)
    for i in range(len1):
        elem = lst_keys[i]
        str_elem = str(elem)
        count_of = work_line[elem]
        if work_line[elem] == 0:
            continue
        #print("in: ", str(elem), ", ",to_line(work_line))
        if elem == 0:
            if 0 in work_line.keys():
                work_line[0] -=count_of
            #print("sub 0: ", to_line(work_line))
            new_line[1] += count_of
            #print("add 1:",to_line(new_line))
        elif len(str_elem)%2 == 0:
            var = list(str_elem)
            pos = len(var)//2
            dgt1, dgt2 = '',''
            ind, flag = 0, 0
            for dgt in var:
                if ind < pos:
                    dgt1 += dgt
                elif int(dgt) > 0 and flag == 0:
                    flag = 1
                    dgt2 +=dgt
                elif flag:
                    dgt2 +=dgt
                ind +=1
            if dgt2 =='':
                dgt2 = 0
            work_line[elem] -=count_of
            #print("sub old: ", to_line(work_line))
            new_line[int(dgt1)] +=count_of
            #print("add p1: ",to_line(new_line))
            new_line[int(dgt2)] +=count_of
            #print("add p2: ",to_line(new_line))
        else:
            work_line[elem] -=count_of
            #print("sub old: ", to_line(work_line))
            new_line[elem*2024] +=count_of
            #print("mul: ", to_line(new_line))
    str_data =''
    for key, val in new_line.items():
        work_line[key] += val
    for key, val in work_line.items():
        if val == 0:
            continue
        str_data += str(key) + ':' +str(val) + ', '
    ansf.write(str_data +"\n")
ansf.close()
print("ans:", sum(work_line.values()))
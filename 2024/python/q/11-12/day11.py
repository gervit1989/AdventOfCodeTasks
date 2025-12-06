
def read_data():
    in_data = []
    with open("in.txt", "r") as fin:
        in_data = list(map(int, fin.readline().strip().split()))
    return in_data

init_line = read_data()
blinks = 75
print(*init_line)
work_line = init_line
res_line =[]
ansf = open("ans.txt",'w')
for varc in range(blinks):
    print(varc)
    res_line = []
    for elem in work_line:
        if elem =='0' or elem == 0:
            res_line.append('1')
        elif len(str(elem))%2 == 0:
            var = list(str(elem))
            pos = len(str(elem))//2
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
            res_line.append(int(dgt1))
            res_line.append(int(dgt2))
        else:
            res_line.append(2024*int(elem))
    work_line = res_line.copy()
    # str_data =''
    # for elem in res_line:
    #     str_data += str(elem) + ' '
    # ansf.write(str_data +"\n")
ansf.close()
print("ans:", len(res_line))
# чтение данных
def read_data(file_name: str):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

# правило 1
def rule1(key1: str, elem: int):
    elem1 = elem
    if key1 == 'turn on':
        elem1 = 1
    elif key1 == 'toggle':
        elem1 = (elem + 1) % 2
    elif key1 == 'turn off':
        elem1 = 0
    return elem1

# правило 2
def rule2(key1: str, elem: int):
    elem1 = elem
    if key1 == 'turn on':
        elem1 += 1
    elif key1 == 'toggle':
        elem1 += 2
    elif key1 == 'turn off':
        elem1 = max(0, elem - 1)
    return elem1


# часть 1
def part1_of_task(arg_name: str, rule_num: int):
    in_arr = read_data(arg_name)
    sum_ans = 0
    matrix = []
    mat_size = 1000
    for i in range(mat_size):
        matrix.append([0 for j in range(mat_size)])
    for row in in_arr:
        lst1 = row.split(" ")
        key1 = ''
        p1 = ''
        p2 = ''
        for i in range(len(lst1)):
            str_var = lst1[i]
            if str_var.count(','):
                if p1 == '':
                    p1 = str_var
                    for j in range(i):
                        if j == 1:
                            key1 += ' '
                        key1 += lst1[j]
                else:
                    p2 = str_var
        p1lst = p1.split(',')
        istart = int(p1lst[0])
        jstart = int(p1lst[1])
        p2lst = p2.split(',')
        ifin = int(p2lst[0])+1
        jfin = int(p2lst[1])+1
        # if ifin == istart or jfin == jstart:

        #print(key1, istart, jstart, ifin, jfin)
        for i in range(istart, ifin):
            for j in range(jstart, jfin):
                if rule_num == 1:
                    matrix[i][j] = rule1(key1, matrix[i][j])
                elif rule_num == 2:
                    matrix[i][j] = rule2(key1, matrix[i][j])
    for i in range(mat_size):
        for j in range(mat_size):
            sum_ans += matrix[i][j]
    print('ans of part1:= ', sum_ans)


file_name = 'input.txt'
part1_of_task(file_name, 1)
part1_of_task(file_name, 2) # 2003292 is low

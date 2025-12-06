def check_str(line, lst_for_find):
    if len(line) == 0:
        return 0
    for elem in lst_for_find:
        if line == elem:
            return 1
    return 0
is_used = 0
used_indexes = []

def check_pos(matriza, pos, lst_data, ends):
    ch = matriza[i][j]
    print(ch, end=" ")
    length_of = len(lst_data[0])
    line_h =''
    line_v = ''
    line_diag1=''
    line_diag2 =''
    is_hor = False
    indexes_h=[]
    indexes_v =[]
    indexes_d=[]
    indexes_d2=[]
    if pos[1] <= ends[1] - length_of:
        for shift in range(length_of):
            line_h+=matriza[pos[0]][pos[1]+shift]
            indexes_h.append((pos[0],pos[1]+shift))
        is_hor = True
    if pos[0] <= ends[0] - length_of:
        is_diag2 =False
        if pos[1] >= length_of-1:
            is_diag2 = True
        for shift in range(length_of):
            line_v +=matriza[shift+pos[0]][pos[1]]
            indexes_v.append((pos[0]+shift,pos[1]))
            if is_hor:
                line_diag1 +=matriza[pos[0]+shift][pos[1]+shift]
                indexes_d.append((pos[0]+shift,pos[1]+shift))
            if is_diag2:
                line_diag2 +=matriza[pos[0]+shift][pos[1]-shift]
                indexes_d2.append((pos[0]+shift,pos[1]-shift))
    var_count = 0
    res = check_str(line_h,lst_data)
    global used_indexes
    global is_used
    if res and is_used:
        for elem in indexes_h:
            if used_indexes.count(elem)>0:
                continue
            used_indexes.append(elem)
    var_count +=res
    res= check_str(line_v,lst_data)
    if res and is_used:
        for elem in indexes_v:
            if used_indexes.count(elem)>0:
                continue
            used_indexes.append(elem)
    var_count +=res
    res = check_str(line_diag1,lst_data)
    if res and is_used:
        for elem in indexes_d:
            if used_indexes.count(elem)>0:
                continue
            used_indexes.append(elem)
    var_count +=res
    res = check_str(line_diag2,lst_data)
    if res and is_used:
        for elem in indexes_d2:
            if used_indexes.count(elem)>0:
                continue
            used_indexes.append(elem)
    var_count +=res
    print(pos,"hor: ",line_h, "vert: ",line_v, "diag1: ",line_diag1, "diag2: ",line_diag2, "res: ", var_count)
    return var_count

lines = []
with open("in.txt", "r") as file:
    lines = file.readlines()
print(lines)
find_txt =["XMAS", "SAMX"]
matrix = []
n_min = -1
n_max = -1
m = len(lines)
for line in lines:
    symbols = list(line)
    matrix.append(symbols)
    n = len(symbols)
    if n<=0:
        continue
    if n_min == -1 or n_min>n:
        n_min = n
    if n_max == -1 or n_max>n:
        n_max = n
print(m, n_min, n_max)
count_n = n_max
if  not (n_max == n_min):
    print("err in counts")
end_lst = (m, count_n)
sum_var = 0
for i in range(m):
    for j in range(count_n):
        sum_var +=check_pos(matrix, (i, j), find_txt, end_lst)
        #break
    #break
print(sum_var)
if is_used:
    print(used_indexes)
    for i in range(m):
        for j in range(count_n):
            if used_indexes.count((i,j)) == 0:
                print(".", end="")
            else:
                print(matrix[i][j], end="")
        print("\n")
#ans1 = 2378

def is_valid_pos(position, lens):
    if 0<=position[0]<lens[0] and 0<=position[1]<lens[1] :
        return True
    return False

lines =[]
matrix =[]
with open("in.txt", "r") as file:
    lines = file.readlines()
for i in range(len(lines)):
    matrix.append( list(lines[i].strip()))
print(matrix, sep="\n")
rows = len(matrix)
cols = len(matrix[0])
lens =[rows, cols]
print("lens: ",lens)
finders = ['0', '9']
key_pos_cur = {}
key_pos_old = {}
pred_val = '0'
for k in range(1, 10):
    print(k)
    key_pos_old = key_pos_cur.copy()
    key_pos_cur ={}
    str_val = str(k)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == str_val:
                lst = []
                print("x: ",(i,j))
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for direct in directions:
                    print(dir)
                    if not is_valid_pos([i+direct[0], j+direct[1]], lens):
                        continue
                    elem = matrix[i+direct[0]][ j+direct[1]]
                    print("dat: ", direct, elem)
                    if elem == pred_val:
                        cur_pos = (i+direct[0], j+direct[1])
                        if elem == '0':
                            lst.append(cur_pos)
                        else:
                            if cur_pos in key_pos_old.keys():
                                print("in keys")
                                for elems in key_pos_old[cur_pos]:
                                    lst.append(elems)
                if len(lst):
                    key_pos_cur[(i, j)] = lst
    pred_val = str_val
    print("cur", key_pos_cur)
    print("old", key_pos_old)
sum_var = 0
ans_map = {}
for key, val in key_pos_cur.items():
    for elem in val:
        if elem in ans_map.keys():
            if not ans_map[elem].count(key):
                ans_map[elem].append(key)
        else:
            ans_map[elem] = [key]
ans_map = dict(sorted(ans_map.items()))
for key, value in ans_map.items():
    print(key, ": ", value)
    sum_var+=len(value)
    print(len(value))
print("ans:", sum_var)


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
count_p = 0
map_ant = {}
rows = len(matrix)
cols = len(matrix[0])
symb_lst =[]
for i in range(rows):
    for j in range(cols):
        elem = matrix[i][j]
        if elem.isalnum():
            if elem in map_ant.keys():
                map_ant[elem].append([i,j])
            else:
                map_ant[elem] = [[i,j]]
lens = [rows, cols]
for key, lst in map_ant.items():
    print(key, " :", *lst)
    combinations = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if [lst[i], lst[j]] not in combinations and [lst[j], lst[i]] not in combinations:
                combinations.append([lst[i], lst[j]])
    for elem in combinations:
        direction = [elem[0][0] -elem[1][0], elem[0][1] -elem[1][1]]
        new_p1 = [elem[0][0] + direction[0],elem[0][1] + direction[1]]
        new_p2 = [elem[1][0] - direction[0],elem[1][1] - direction[1]]
        print(elem, new_p1, new_p2, direction)
        if is_valid_pos(new_p1, lens):
            if new_p1 not in symb_lst:
                symb_lst.append(new_p1)
        if is_valid_pos(new_p2, lens):
            if new_p2 not in symb_lst:
                symb_lst.append(new_p2)
        #break
print(*symb_lst)
print("ans:", len(symb_lst))
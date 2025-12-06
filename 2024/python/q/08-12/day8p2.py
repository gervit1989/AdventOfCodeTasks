
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
out1 = open("1.log", "w")
for key, lst in map_ant.items():
    print(key, " :", *lst)
    combinations = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if [lst[i], lst[j]] not in combinations and [lst[j], lst[i]] not in combinations:
                combinations.append([lst[i], lst[j]])
    if len(lst) > 1:
        for elem in lst:
            if elem not in symb_lst:
                symb_lst.append(elem)

    for elem in combinations:
        direction = [elem[0][0] -elem[1][0], elem[0][1] -elem[1][1]]
        new_p1 = elem[0]
        out1.write(str(elem[0]) + "," +str(elem[1]) + "\n")
        out1.write("p1:" + str(new_p1) + ", " + str(direction)+"\n")
        while True:
            new_p1 = [new_p1[0] + direction[0],new_p1[1] + direction[1]]
            out1.write(str(new_p1) + "\n")
            if is_valid_pos(new_p1, lens):
                out1.write("valid\n")
                out1.write(str(symb_lst) + "\n")
                if new_p1 not in symb_lst:
                    symb_lst.append(new_p1)
                    out1.write("app\n")
            else:
                out1.write("broken\n")
                break
        new_p2 = elem[1]
        out1.write("p2:" + str(new_p2) + ", " + str(direction) + "\n")
        while True:
            new_p2 = [new_p2[0] - direction[0],new_p2[1] - direction[1]]
            out1.write(str(new_p2) + "\n")
            if is_valid_pos(new_p2, lens):
                out1.write("valid\n")
                out1.write(str(symb_lst)+"\n")
                if new_p2 not in symb_lst:
                    symb_lst.append(new_p2)
                    out1.write("app\n")
            else:
                out1.write("broken\n")
                break

out1.write("results:\n")
for elem in symb_lst:
    out1.write(str(elem) + "\n")
out1.close()
print("ans:", len(symb_lst))

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
print(*lens)
out1 = open("2.log", "w")
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
        opers=['+','-']
        out1.write(str(elem[0]) + "," +str(elem[1]) + "\n")
        for k in range(2):
            new_p = [elem[k][0], elem[k][1]]
            out1.write("p" +str(k+1) +":" +str(new_p) + ", " + str(direction)+"\n")
            while True:
                for l1 in range(2):
                    str_val =(str(new_p[l1]) + opers[k] + "(" + str(direction[l1])+")")
                    new_p[l1] = int(eval(str_val))
                out1.write(str(new_p)+"\n")
                if is_valid_pos(new_p, lens):
                    out1.write("valid\n")
                    out1.write(str(symb_lst)+"\n")
                    if new_p not in symb_lst:
                        #symb_lst.append([new_p[0], new_p[1]]) # так ответ верный
                        symb_lst.append(new_p) #- так ответ неверный
                        out1.write("app\n")
                else:
                    out1.write("broken\n")
                    break

out1.write("results:\n")
for elem in symb_lst:
    out1.write(str(elem) + "\n")
out1.close()
print("ans:", len(symb_lst))
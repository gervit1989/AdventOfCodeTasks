from itertools import count


def print_state(m, row_count,col_count):
    for i in range(row_count):
        strv=''
        for j in range(col_count):
            strv+=m[i][j]
        print(i, strv)

motions = ''
matr = []
addr ='in.txt'
with open(addr, 'r') as fin:
    flag = False
    while True:
        line = fin.readline().strip()
        if len(line) == 0 or line == " ":
            if flag:
                break
            flag = True
        if flag:
            motions+=line
        else:
            matr.append(list(line))
rows = len(matr)
cols = len(matr[0])
print(rows, cols)
print(motions)
print_state(matr, rows, cols)
robot_pos =(0,0)
robot_inited = False
box = 'O'
wall ='#'
free_place = '.'
for i in range(rows):
    for j in range(cols):
        if matr[i][j] =='@':
            robot_pos=(i,j)
            robot_inited =True
            break
    if robot_inited:
        break
motions_map = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
for move in motions:
    direction =motions_map[move]
    print(move)
    pos_new = (robot_pos[0] + direction[0], robot_pos[1] +direction[1])
    elem = matr[pos_new[0]][pos_new[1]]
    print(pos_new, elem, robot_pos)
    if elem == wall:
        continue
    elif elem == free_place:
        matr[pos_new[0]][pos_new[1]] = '@'
        matr[robot_pos[0]][robot_pos[1]] = free_place
        robot_pos = pos_new
    elif elem == box:
        count_box = 1
        lst=[pos_new]
        while True:
            pos_new = (pos_new[0] + direction[0], pos_new[1] +direction[1])
            lst.append(pos_new)
            elem = matr[pos_new[0]][pos_new[1]]
            if elem == wall:
                break
            elif elem == free_place:
                #print("zq", count_box)
                matr[robot_pos[0]][robot_pos[1]] = free_place
                robot_pos = lst[0]
                matr[robot_pos[0]][robot_pos[1]] = '@'
                for k in range(count_box):
                    ind = lst[k+1]
                    matr[ind[0]][ind[1]] = box
                break
            else:
                count_box+=1
    print_state(matr, rows, cols)
answer1 = 0
for i in range(rows):
    for j in range(cols):
        if matr[i][j] == box:
            answer1 += 100*i+j
print("answ1: ", answer1)


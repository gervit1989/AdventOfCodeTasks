from multiprocessing.connection import answer_challenge
from operator import index

def is_pos_in_area(position, lens):
    is_in_area = True
    if position[0] <0 or position[0]>=lens[0]:
        is_in_area = False
    if position[1] <0 or position[1]>=lens[1]:
        is_in_area = False
    return is_in_area

def turn_dir(dir_var):
    turns_map ={
        (-1, 0):(0,1),
        (0, 1): (1, 0),
        (1, 0): (0,-1),
        (0, -1):(-1,0)
    }
    if dir_var in turns_map.keys():
        for key, value in turns_map.items():
            if key == dir_var:
                return value
    else:
        print("errr")
    return (0, 0)

def step_to(pos_from, matr, lens, direct):
    ans = []
    new_row =pos_from[0] + direct[0]
    new_col = pos_from[1] + direct[1]
    pos_new_ = [new_row, new_col]
    if not is_pos_in_area(pos_new_, lens):
        ans.append(2)
        ans.append(direct)
        ans.append(pos_new_)
        return ans
    elif matr[new_row][new_col] == "#":
        new_dir = turn_dir(direct)
        ans = step_to(pos_from, matr, lens, new_dir)
    else:
        ans.append(1)
        ans.append(direct)
        ans.append(pos_new_)
    return ans

def game(pos0, matr, leng, dir_var):
    pos_ = pos0
    #print("pos: ",pos_)
    ans = []
    dir_cur = dir_var
    way_list =[]
    way_list.append(pos_)
    is_writer = 0
    out1 = None
    if is_writer:
        out1=open("way.txt", "w")
        out1.write("pos: " +str(pos_)+"\n")
    while True:
        info = step_to(pos_, matr, leng, dir_cur)
        if info[0] == 0:
            print("tupik")
            break
        elif info[0] == 2:
            matr[pos_[0]][pos_[1]] = "X"
            pos_ = info[2]
            # print("pos: ",pos_)
            break
        else:
            dir_cur = info[1]
            pos_ = info[2]
            if pos_ in way_list:
                way_reverse = way_list[-1:0:-1] + [way_list[0]]
                if is_writer:
                    out1.write(str(way_reverse)+"\n")
                pos_check = way_reverse.index(pos_)
                info1 = step_to(pos_, matr, leng, dir_cur)
                if info1[0] == 1:
                    if is_writer:
                        out1.write(str(way_reverse[pos_check-1]) +", " +str(info1[2])+"\n")
                    if way_reverse[pos_check-1] == info1[2]:
                        ans.append(True)
                        ans.append(way_list)
                        return ans
            way_list.append(pos_)
            if is_writer:
                out1.write("pos: " +str(pos_) + "\n")
    if is_writer:
        out1.write("End")
        out1.close()
    ans.append(False)
    ans.append(way_list)
    return ans

lines =[]
matrix =[]
with open("in.txt", "r") as file:
    lines = file.readlines()
for i in range(len(lines)):
    matrix.append( list(lines[i].strip()))
print(matrix, sep="\n")
step_count = 0
pos_init = [-1,-1]
rows = len(matrix)
cols = len((matrix[0]))

for i in range(rows):
    print(matrix[i])
    if matrix[i].count('^'):
        pos_init=[i,matrix[i].index('^')]
        break
lengths = [rows, cols]
print("lens: ",lengths)
variants = 0
testspos = [(6,3), (7,6), (7,7),(8,1), (8,3), (9,7)]
#i,j = testspos[5]

direction = (-1, 0)
# Путь
answer = game(pos_init, matrix, lengths, direction)

way_var = []
for elem in answer[1]:
    if elem in way_var:
        continue
    way_var.append(elem)

index_var = 0
while True:
    direction = (-1, 0)
    i,j = way_var[index_var]
    elem = matrix[i][j]
    if elem == "#" or elem == "^":
        index_var += 1
        continue
    print("new #:", [i,j], len(way_var), index_var, end=" ")
    matrix[i][j] ="#"
    answer = game(pos_init, matrix, lengths, direction)
    is_cycled = answer[0]
    print("\n")
    matrix[i][j] = elem
    for elem1 in answer[1]:
        if elem1 in way_var:
            continue
        way_var.append(elem1)
    if is_cycled:
        print("cycled\n")
        variants += 1
    index_var +=1
    if index_var == len(way_var):
        print("found!!!")
        break
print("ans: ",variants)
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
    #(-1, 0) ->(0,1)
    #(0, 1)  ->(1, 0)
    #(1, 0)  ->(0,-1)
    #(0, -1) ->(-1,0)
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
    print("pos in check: ", pos_new_)
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
direction = (-1,0)
lengths = [rows, cols]
print("lens: ",lengths)
pos_ = pos_init
print("pos: ",pos_)
step_count+=1
point_lst = []
point_lst.append(pos_)
while True:
    info = step_to(pos_, matrix, lengths, direction)
    if info[0] ==0:
        print("tupik")
        break
    elif info[0] == 2:
        matrix[pos_[0]][pos_[1]] = "X"
        pos_ = info[2]
        print("pos: ",pos_)
        break
    else:
        step_count +=1
        direction = info[1]
        pos_ = info[2]
        if not point_lst.count(pos_):
            point_lst.append(pos_)
        print("pos: ",pos_, "steps: ", step_count)
        matrix[pos_[0]][pos_[1]] = "X"
print("ans: ",step_count, "points: ", len(point_lst))
#point_lst.sort()
#print(point_lst)
out = open("ans.txt", "w")
x_count = 0
point_lst2 =[]
for i in range(rows):
    str_var = ""
    for j in range(cols):
        str_var +=str(matrix[i][j])
        if matrix[i][j] =="X":
            x_count+=1
            if not point_lst2.count([i,j]):
                point_lst2.append([i,j])
    str_var +=("\n")
    out.write(str_var)
out.close()
print("\nx: ",x_count)
#point_lst2.sort()
#print(point_lst2)
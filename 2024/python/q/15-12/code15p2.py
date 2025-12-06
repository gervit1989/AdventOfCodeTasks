from itertools import count

box = 'O'
box_lst = ['[',']']
wall ='#'
free_place = '.'
def sum_points(p1, p2):
    #print("sump: ",p1,p2)
    p= [p1[0]+(p2[0]), p1[1]+(p2[1])]
    print("res: ", p)
    return p

def find_next_box_in_dir(cur, m, dir):
    pos1 = cur
    lst =[]
    print("pos3")
    pos3 =sum_points(pos1,dir)
    elem1 = m[pos3[0]][pos3[1]]
    elem2 = None
    if dir[1] == 0:
        print("pos2")
        pos2 = sum_points(cur,(0,1))
        print("pos4")
        pos4 =sum_points(pos2,dir)
        elem2 = m[pos4[0]][pos4[1]]
    flag_wall = False
    print(elem1, elem2)
    if elem1 == wall:
        flag_wall = True
    elif elem1 in box_lst:
        pos3r =pos3 if elem1 == box_lst[0] else sum_points(pos3, (0,-1))
        lst2 =find_next_box_in_dir(pos3r, m,dir)
        print(lst2)
        lst2len =len(lst2)
        if lst2len>1:
            lst.append([pos3r,lst2[0:lst2len-1]])
        else:
            lst.append([pos3r])
        print(lst)
        if lst2[-1]:
            flag_wall = True
    if elem2 == free_place:
        lst.append([pos4, False, elem])
    elif elem2 in box_lst:
        pos4r =pos4 if elem2 == box_lst[0] else sum_points(pos4,(0,-1))
        lst2 =find_next_box_in_dir(pos4r, m,dir)
        lst.append([pos4r,lst2])
        if lst2[-1] == 0:
            flag_wall = True
    lst.append(flag_wall)
    return lst

class Box:
    def __init__(self, cur):
        self.map_moves ={}
        self.point = (cur[0], cur[1])

    def get_n_in_dir_while(self, move, lst_of_boxes):
        pass

def print_state(m, row_count,col_count):
    for i in range(row_count):
        strv=''
        for j in range(col_count):
            strv+=m[i][j]
        print(i, strv)

motions = ''
matr = []
addr ='in11.txt'
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
matr2=[]
boxes = []
for i in range(rows):
    lsst = []
    for j in range(cols):
        elem = matr[i][j]
        if elem =='@':
            robot_pos=[i,2*j]
            robot_inited =True
            lsst.append(elem)
            lsst.append(free_place)
        elif elem == box:
            lsst += box_lst
            boxes.append((i,j))
        else:
            lsst.append(elem)
            lsst.append(elem)
    matr2.append(lsst)
rows2 = len(matr2)
cols2 = len(matr2[0])
print("new: ", rows2, cols2)
print_state(matr2, rows2, cols2)
motions_map = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
for move in motions:
    direction =motions_map[move]
    print(move)
    pos_new = sum_points(robot_pos, direction)
    elem = matr2[pos_new[0]][pos_new[1]]
    print("zzz",pos_new, elem, robot_pos)
    if elem == wall:
        continue
    elif elem == free_place:
        matr2[pos_new[0]][pos_new[1]] = '@'
        matr2[robot_pos[0]][robot_pos[1]] = free_place
        robot_pos = pos_new
    elif elem in box_lst:
        init_pos =pos_new if elem==box_lst[0] else sum_points(pos_new,[0,-1])
        print(init_pos)
        ans_lst = find_next_box_in_dir(init_pos, matr2, direction)
        print(ans_lst)
        if ans_lst[-1] == True:
            print("wall")
            continue
        else:
            print("dot")
            for i in range(2):
                pass
            pass
    print_state(matr, rows, cols)
answer2 = 0
for i in range(rows2):
    for j in range(cols2):
        if matr2[i][j] == box_lst[0]:
            answer2 += 100*i+j
print("answ1: ", answer2)

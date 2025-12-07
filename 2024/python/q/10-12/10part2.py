
def is_valid_pos(position, lens):
    if 0<=position[0]<lens[0] and 0<=position[1]<lens[1] :
        return True
    return False

directions = [(-1,0),(0,-1),(0,1),(1,0)]

def build_ways(matr, pos_from, lens):
    way_lst = []
    print(pos_from)
    for direct in directions:
        new_pos =(pos_from[0] + direct[0], pos_from[1] + direct[1])
        if not is_valid_pos(new_pos, lens):
            continue
        if matr[new_pos[0]][new_pos[1]] == '1':
            way_lst.append([new_pos])
    print(way_lst)
    for ind in range(2, 10):
        str_val_ = str(ind)
        len1 = len(way_lst)
        #print(len1, str_val_)
        for ind in range(len1):
            pos0 = way_lst[ind][-1]
            id_var = 0
            for direct in directions:
                new_pos =(pos0[0] + direct[0], pos0[1] + direct[1])
                if not is_valid_pos(new_pos, lens):
                    continue
                if matr[new_pos[0]][new_pos[1]] == str_val_:
                    if id_var == 0:
                        way_lst[ind].append(new_pos)
                    else:
                        lst = way_lst[ind].copy()
                        lst[-1] = new_pos
                        way_lst.append(lst)
                    id_var+=1
        #print(way_lst)
    print(way_lst)
    final_data =[]
    for lst in way_lst:
        if len(lst) == 9:
            final_data.append(lst)
    return final_data

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
sum_var = 0
for i in range(rows):
    for j in range(cols):
        # if i != 6 and j != 0:
        #     continue
        if matrix[i][j] == '0':
            ways = build_ways(matrix, (i,j), lens)
            sum_var+=len(ways)
            print("len ", (i,j), ": ", len(ways))
            #break
print("ans:", sum_var)

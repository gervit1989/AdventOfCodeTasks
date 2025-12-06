
def is_valid_pos(position, lens):
    if 0<=position[0]<lens[0] and 0<=position[1]<lens[1] :
        return True
    return False

directions = [(-1,0),(0,-1),(0,1),(1,0)]

class Reg:
    def find_next(self, item, lst, ind=-1):
        for dir in directions:
            pos_new = (item[0]+dir[0], item[1]+dir[1])
            if pos_new in lst:
                if ind == -1:
                    if pos_new in self.data:
                        pass
                    else:
                        self.data.append(pos_new)
                        self.find_next(pos_new, lst, ind)
                else:
                    if pos_new in self.regs[ind]:
                        pass
                    else:
                        self.regs[ind].append(pos_new)
                        self.find_next(pos_new, lst, ind)
    def __init__(self, name, lst,lens=None):
        self.name = name
        self.data = []
        self.regs = []
        out1 =open("out"+str(name)+".txt", 'w+')
        for item in lst:
            out1.write(str(item) + "\n")
            if item in self.data:
                continue
            if item == lst[0]:
                self.data.append(item)
                self.find_next(item, lst, -1)
            else:
                is_in_any_reg = False
                for element in self.regs:
                    if item in element:
                        is_in_any_reg = True
                        break
                if is_in_any_reg:
                    continue
                len1 = len(self.regs)
                self.regs.append([item])
                self.find_next(item, lst, len1)
            out1.write(str(self.data) + "\n" + str(self.regs) + "\n")
        out1.close()
        if lens is not None:
            lst2 = self.data.copy()
            self.data = []
            for irow in range(lens[0]):
                for icol in range(lens[1]):
                    if (irow, icol) in lst2:
                        self.data.append((irow, icol))
            for ix in range(len(self.regs)):
                lst2 = self.regs[ix].copy()
                self.regs[ix] = []
                for irow in range(lens[0]):
                    for icol in range(lens[1]):
                        if (irow, icol) in lst2:
                            self.regs[ix].append((irow, icol))

    def isSolid(self):
        return (True if len(self.regs) == 0 else False)
    def calc_square(self):
        return len(self.data)
    def calc_perimeter(self):
        perim = 0
        for item in self.data:
            for dir in directions:
                pos_new = (item[0]+dir[0], item[1]+dir[1])
                if pos_new not in self.data:
                    perim +=1
        return perim
    def calc_perimeter2(self):
        stor_map = []
        stors = []
        is_dbg = True
        if is_dbg:
            print(self.name)
        for item in self.data:
            for dir in directions:
                pos_new = (item[0]+dir[0], item[1]+dir[1])
                if pos_new not in self.data:
                    is_in_map = False
                    if is_dbg:
                        print(item,"dir: ", dir," pos: ", pos_new, " neighbours: ", stor_map, " keys: ", stors)
                    for ind in range(len(stors)):
                        val_key =stors[ind]
                        if dir == val_key[0]:
                            if is_dbg:
                                print("x")
                            if item[0] == val_key[1][0] or item[1] == val_key[1][1]:
                                if is_dbg:
                                    print("y")
                                is_in_map = False
                                if dir[0] == 0:
                                    if is_dbg:
                                        print("y1")
                                    if (item[0] -1, item[1]) in stor_map[ind]:
                                        is_in_map =True
                                    elif (item[0]+1, item[1]) in stor_map[ind]:
                                        is_in_map =True
                                if dir[1] == 0:
                                    if is_dbg:
                                        print("y2")
                                    if (item[0], item[1] -1) in stor_map[ind]:
                                        is_in_map =True
                                    elif (item[0], item[1] + 1) in stor_map[ind]:
                                        is_in_map =True
                                if is_in_map:
                                    if is_dbg:
                                        print("in map")
                                    stor_map[ind].append(item)
                                    break
                    if not is_in_map:
                        stors.append((dir, item))
                        stor_map.append([item])
        return len(stors)
    def divide(self):
        xregs = []
        for item in self.regs:
            xregs.append(Reg(self.name, item))
        return xregs
    def to_out(self, lens):
        outx = open("virez "+self.name, "w")
        for irow in range(lens[0]):
            str_val = ''
            for icol in range(lens[1]):
                if (irow, icol) in self.data:
                    str_val+=self.name
                else:
                    str_val+='.'
            outx.write(str_val+"\n")
        outx.close()
    def __str__(self):
        return f"{self.name}, p={self.calc_perimeter()}, sq={self.calc_square()}, p2 ={self.calc_perimeter2()}"

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
names_map ={}
for row in range(rows):
    for col in range(cols):
        elem = matrix[row][col]
        if elem =='.':
            continue
        if elem in names_map.keys():
            names_map[elem].append((row, col))
        else:
            names_map[elem] = [(row, col)]
print(*names_map.items(), sep="\n")
regions = []
for key, val in names_map.items():
    print("create reg ", key)
    area = Reg(key, val, lens)
    if area.isSolid():
        print("solid ", key, val)
        regions.append(area)
    else:
        print("div ", key, val, area.regs)
        regions.append(area)
        regs1 = area.divide()
        print(len(regs1), "len1")
        for item in regs1:
            regions.append(item)
ans_val = 0
ans_val2 = 0
for item in regions:
    print(item)
    item.to_out(lens)
    break
    ans_val += item.calc_perimeter()*item.calc_square()
    ans_val2 += item.calc_perimeter2()*item.calc_square()
print("ans: ", ans_val)
print("ans2: ", ans_val2)
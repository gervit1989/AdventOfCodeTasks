# чтение данных
def read_data(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

class Point:
    def __init__(self, xc,yc):
        self.x=xc
        self.y = yc
    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        return False
    def __str__(self):
        return f"({self.x},{self.y})"
    def move(self, direction:str):
        xc = self.x
        yc = self.y
        if direction =='^':
            yc +=1
        elif direction =='<':
            xc-=1
        elif direction =='v':
            yc-=1
        elif direction =='>':
            xc+=1
        return Point(xc,yc)

# часть 1
def part1_of_task(name_arg):
    in_arr = read_data(name_arg)
    sum_ans = 0
    for row in in_arr:
        lst1 = row.split('=')
        answer = 0
        if len(lst1) > 1:
            answer = int(lst1[1])
        plist = []
        point = Point(0,0)
        plist.append(point)
        dir_lst = list(lst1[0])
        for direction in dir_lst:
            new_point = point.move(direction)
            bflag = False
            for p in plist:
                if p.__eq__(new_point):
                    bflag = True
                    break
            if not bflag:
                plist.append(new_point)
            point = new_point
        #print(*plist)
        answ = len(plist)
        print('on row ', answ, answ-answer)
        sum_ans += answ - answer
    print('ans of part1:= ', sum_ans)

# часть 2
def part2_of_task(name_arg):
    in_arr = read_data(name_arg)
    for row in in_arr:
        lst1 = row.split('=')
        plist = []
        point = Point(0,0)
        point2 = Point(0,0)
        plist.append(point)
        dir_lst = list(lst1[0])
        len_lst = len(dir_lst)
        dir_lst1 = [dir_lst[i] for i in range(len_lst) if i%2==0]
        dir_lst2 = [dir_lst[i] for i in range(len_lst) if i%2==1]
        for direction in dir_lst1:
            new_point = point.move(direction)
            bflag = False
            for p in plist:
                if p.__eq__(new_point):
                    bflag = True
                    break
            if not bflag:
                plist.append(new_point)
            point = new_point
        for direction in dir_lst2:
            new_point = point2.move(direction)
            bflag = False
            for p in plist:
                if p.__eq__(new_point):
                    bflag = True
                    break
            if not bflag:
                plist.append(new_point)
            point2 = new_point
        answ = len(plist)
        answer = 0
        if len(lst1) > 1:
            answer = int(lst1[1])
        print('on row ', answ, answ-answer)

fname='input.txt'
part1_of_task(fname)
part2_of_task(fname)
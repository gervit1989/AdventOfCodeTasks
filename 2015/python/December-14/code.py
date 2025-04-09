# импорт
from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

def is_empty(row:str='')->bool:
    if len(row) == 0 or row=='':
        return True
    return False

class FlyObj:
    def __init__(self, instr:str=''):
        if is_empty(instr):
            self.name = ''
            self.vel = 0
            self.fly = 0
            self.rest = 0
        else:
            lst = instr.strip().split(' ')
            self.name = lst[0]
            self.vel = float(lst[3])
            self.fly = float(lst[6])
            self.rest = float(lst[-2])
        pass

    def get_dist_by_time(self, time:float)->float:
        z_count = int(time/(self.fly+self.rest))
        ztime =z_count * (self.fly+self.rest)
        dist = z_count * self.fly * self.vel
        diff = time-ztime
        if diff > self.fly:
            dist += self.fly * self.vel
        else:
            dist += diff *self.vel
        return dist

    def get_name(self):
        return self.name


# расчет
def calc_ans(lines:list[str]=None, irule:int=0):
    ans=0
    objects = []
    for line in lines:
        row = line.strip()
        if is_empty(row):
            continue
        print(row)
        objects.append(FlyObj(row))

    max_name = ''
    max_dist = 0
    for obj in objects:
        dist = obj.get_dist_by_time(2503)
        print(obj.get_name(), dist)
        if is_empty(max_name) or dist > max_dist:
            max_name = obj.get_name()
            max_dist = dist

    print("answer"+str(irule)+":", max_dist, max_name)

# входные данные
in_put = read_data_from_serv(2015, 14)
#in_put = read_data_from_file('in.txt')

# вычисление
calc_ans(in_put, 1)
#calc_ans(in_put, 2)
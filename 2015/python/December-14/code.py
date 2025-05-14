# импорт
from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file


def is_empty(row: str = '') -> bool:
    if len(row) == 0 or row == '':
        return True
    return False


class FlyObj:
    def __init__(self, instr: str = ''):
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
        self.degree = 0
        self.cur_dist = 0

    def get_dist_by_time(self, time: float) -> float:
        z_count = int(time / (self.fly + self.rest))
        ztime = z_count * (self.fly + self.rest)
        dist = z_count * self.fly * self.vel
        diff = time - ztime
        if diff > self.fly:
            dist += self.fly * self.vel
        else:
            dist += diff * self.vel
        self.cur_dist = dist
        return dist

    def get_name(self):
        return self.name

    def get_cur_dist(self):
        return self.cur_dist

    def get_degree(self):
        return self.degree

    def app_degree(self, deg):
        self.degree += deg


# расчет
def calc_ans(lines: list[str] = None, irule: int = 0):
    ans = 0
    objects = []
    for line in lines:
        row = line.strip()
        if is_empty(row):
            continue
        print(row)
        objects.append(FlyObj(row))

    step = 0
    time_end = 2503
    if irule == 1:
        step = time_end
    elif irule == 2:
        step = 1
    time_cur = 0
    all_max_obj = None
    with open('code.log', 'w') as fout:
        while True:
            max_obj = None
            max_name = ''
            max_dist = 0
            print("Cur Time: ", time_cur)
            fout.write("Cur Time: "+str(time_cur)+"\n")
            for obj in objects:
                dist = obj.get_dist_by_time(time_cur+step)
                fout.write(obj.get_name() +";" +str(dist) +";" + str(obj.get_degree()) + '\n')
                if is_empty(max_name) or dist > max_dist:
                    max_name = obj.get_name()
                    max_dist = dist
                    max_obj = obj
            if irule ==2:
                for obj in objects:
                    dist = obj.get_cur_dist()
                    if dist == max_obj.get_cur_dist():
                        obj.app_degree(1)
            else:
                max_obj.app_degree(1)
            print("max on step: ", max_obj.get_name())
            fout.write("max on step: " +max_obj.get_name() +'\n')

            if step+time_cur >=time_end:
                break
            else:
                time_cur += step
    max_deg = 0
    for obj in objects:
        deg = obj.get_degree()
        if max_deg == 0 or deg >max_deg:
            all_max_obj = obj
            max_deg = deg
    print("answer" + str(irule) + ":", all_max_obj.get_name(), all_max_obj.get_cur_dist(), all_max_obj.get_degree())


# входные данные
in_put = read_data_from_serv(2015, 14)
# in_put = read_data_from_file('in.txt')

# вычисление
calc_ans(in_put, 1)
calc_ans(in_put, 2) #647 is low

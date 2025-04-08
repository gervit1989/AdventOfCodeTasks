from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

# определение строки
def get_info(in_str:str=''):
    lst = in_str.strip().split(' ')
    ans = dict()
    ans['p1'] = lst[0]
    ans['p2'] = lst[-1][0:-1]
    distance = int(lst[3])
    if lst[2] == 'lose':
        distance *= -1
    ans['dist'] = distance

    return ans

# расстояние между соседями
class NeighbDist:
    # инициализация
    def __init__(self, line:str='',p1:str='', p2:str=''):
        if line == '':
            self.persona1 = p1
            self.persona2 = p2
            self.dist = 0
        else:
            info = get_info(line)
            self.persona1 = info['p1']
            self.persona2 = info['p2']
            self.dist12 = info['dist']
            self.dist21 = 0
            self.dist = self.dist12
        self.was_flag = False

    #флаг
    def get_flag(self):
        return  self.was_flag

    def set_flag(self, flag:bool=False):
        self.was_flag = flag

    def add_info(self, dist:float=0):
        self.dist21 = dist
        #print('add info ', dist)
        self.dist = self.dist12 + self.dist21

    # расстояние
    def get_other(self, p):
        if p == self.persona1:
            return self.persona2
        elif p == self.persona2:
            return self.persona1
        return None

    def get_persona1(self):
        return self.persona1

    def get_persona2(self):
        return self.persona2

    def get_distance_from(self, p):
        if p == self.persona1 or p == self.persona2:
            return self.dist
        return None

    def get_dist(self):
        return self.dist

    def get_distance(self, pers1, pers2):
        if pers1 == self.persona1 and pers2 == self.persona2:
            return self.dist
        elif pers1 == self.persona2 and pers2 == self.persona1:
            return self.dist
        return None


# алгоритм дейкстры
def deixstra(init_neighb:str= '', dists:list[NeighbDist]=None, neighbours:list[str]=None, irule:int=0,cycled:bool=False):
    if init_neighb == '' or dists is None or neighbours is None:
        return 0
    lst_ans=[0,]
    nei_lst = []
    nei_lst.append(init_neighb)
    while len(nei_lst) < len(neighbours):
        next_obj = ''
        min_dst = -1
        jdist = -1
        for idist in range(len(dists)):
            distance = dists[idist]
            if distance.get_flag():
                continue
            dst_var = distance.get_distance_from(init_neighb)
            other_obj = distance.get_other(init_neighb)
            if dst_var is None or other_obj in nei_lst:
                continue
            elif min_dst < 0 or (min_dst <= dst_var and irule == 1):
                min_dst = dst_var
                next_obj = other_obj
                jdist = idist
        if jdist>=0 and jdist<len(dists):
            dists[jdist].set_flag(True)
            nei_lst.append(next_obj)
            lst_ans[0] += min_dst
            #print("\t",min_dst, init_city, next_city)
            init_neighb = next_obj
    lst_ans.append(' -> '.join(nei_lst))
    #print(lst_ans)
    return lst_ans


class Way:
    def __init__(self, init_p:str='', nodes:list[str]=None, dists:list[float]=None):
        if nodes is not None:
            self.nodes = nodes.copy()
        else:
            self.nodes =[]
            self.nodes.append(init_p)
        if dists is not None:
            self.dists = dists.copy()
        else:
            self.dists = []

    def get_first(self)->str:
        return self.nodes[0]

    def get_last(self)->str:
        return self.nodes[-1]

    def get_nodes(self)->list[str]:
        return self.nodes

    def get_dists(self)->list[float]:
        return self.dists

    def get_in_state(self, obj)->bool:
        if obj in self.nodes:
            return True
        return False

    def correct(self, dists:list[NeighbDist]=None):
        pos = self.nodes.index('Iam')
        new_val = 0
        for dst in dists:
            state = dst.get_distance(self.nodes[pos-1], self.nodes[pos+1])
            if state is not None:
                new_val = 0 if state>0 else state
                break
        self.dists[pos-1] =new_val
        pass


def get_max_cycled_way(init_neighb:str= '', dists:list[NeighbDist]=None, neighbours:list[str]=None):
    if init_neighb == '' or dists is None or neighbours is None:
        return 0
    lst_ways = []
    lst_ways.append(Way(init_neighb))
    while True:
        new_ways = []
        for way in lst_ways:
            cur_obj = way.get_last()
            # print('name:',cur_obj)
            for dst in dists:
                dist = dst.get_distance_from(cur_obj)
                if dist is not None:
                    other = dst.get_other(cur_obj)
                    if way.get_in_state(other):
                        continue
                    else:
                        way_dists = way.get_dists().copy()
                        way_dists.append(dist)
                        way_nodes = way.get_nodes().copy()
                        way_nodes.append(other)
                        new_way = Way('', way_nodes, way_dists)
                        new_ways.append(new_way)
                else:
                    continue
        # print('end')
        lst_ways.clear()
        lst_ways = new_ways.copy()
        if len(lst_ways[0].get_nodes()) == len(neighbours):
            break
    max_ans = 0
    max_way = None
    # print('x')
    with open('code.log','a+') as fout:
        for way in lst_ways:
            if way.get_in_state('Iam'):
                if way.get_last() == 'Iam':
                    continue
                elif way.get_first() == 'Iam':
                    continue
                else:
                    way.correct(dists)
            for dst in dists:
                dist = dst.get_distance(way.get_first(), way.get_last())
                if dist is not None:
                    ans = sum(way.get_dists())+dist

                    #print(way.get_nodes(), ans)
                    fout.write(str(way.get_nodes()) +"; dists: " +str(way.get_dists())+"; "+str(dist) + "; ans: "+str(ans)+'\n')
                    if max_ans < ans:
                        max_ans = ans
                        max_way = way
                    break
    lst_ans =[]
    lst_ans.append(max_ans)
    lst_ans.append(' -> '.join(max_way.get_nodes()))
    return  lst_ans

def calc_ans(lines:list[str], irule:int=0):
    dists=[]
    persons=set()
    for row in lines:
        if len(row) == 0 or row == '':
            continue
        print(row)
        dst = NeighbDist(row)
        was_flag = False
        for dist in dists:
            if dist.get_persona1() == dst.get_persona2() and dist.get_persona2() == dst.get_persona1():
                was_flag = True
                dist.add_info(dst.get_distance(dst.get_persona1(), dst.get_persona2()))
                break
        if not was_flag:
            dists.append(dst)
            persons.add(dst.get_persona1())
            persons.add(dst.get_persona2())
    min_dist = -1
    way = ''
    objects = list(persons)
    if irule == 11:
        objects.sort()
        for obj in objects:
            dst = NeighbDist('', obj, 'Iam')
            dists.append(dst)
        objects.append('Iam')
    objects.sort()
    print(objects)
    for dst in dists:
        print(dst.get_persona1(), dst.get_persona2(), dst.get_dist())

    if irule>=10:
        with open('code.log','w') as fout:
            fout.write("INFO:\n")
    for obj in objects:
        if obj =='Iam':
            continue
        for dst in dists:
            dst.set_flag(False)
        if irule == 1:
            distance = deixstra(obj, dists, objects, irule, True)
        elif irule >= 10:
            distance = get_max_cycled_way(obj, dists, objects)
        way_cur = distance[1]
        lst = way_cur.split(' ')
        obj1 =lst[0]
        obj2 = lst[-1]
        cycled_dst = 0
        if irule == 1:
            for dst in dists:
                val =dst.get_distance(obj1, obj2)
                if val is not None:
                    cycled_dst=val
                    break
        print(distance, cycled_dst, cycled_dst+distance[0])
        cur_dist =cycled_dst+distance[0]
        if min_dist <0 or (cur_dist > min_dist and irule == 1):
            min_dist = cur_dist
            way = distance[1]
    print("answer:", way, min_dist)

# входные данные
in_put = read_data_from_serv(2015, 13)
#in_put = read_data_from_file('in.txt')

# вычисление
calc_ans(in_put, 10)
calc_ans(in_put, 11)

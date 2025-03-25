from tools.dl import download_input
from tools.dl import read_data_from_file

# чтение данных
def read_data(day: int):
    in_str = download_input(2015, day)
    in_data = in_str.split('\n')
    for i in range(len(in_data)):
        in_data[i] = in_data[i].strip()
    return in_data

# расстояние между городами
class CityDist:
    # инициализация
    def __init__(self, dst:str='', city1:str='', city2:str=''):
        self.distance = int(dst.strip())
        self.city1 = city1
        self.city2 = city2
        self.was_flag = False

    # расстояние
    def get_distance(self, city):
        if city == self.city1 or city == self.city2:
            return  self.distance
        return None

    # расстояние
    def get_other_city(self, city):
        if city == self.city1:
            return self.city2
        if city == self.city2:
            return self.city1
        return None

    def get_city(self, irule:int=0):
        if irule == 1:
            return self.city1
        if irule == 2:
            return self.city2
        return ''

    # расстояние
    def get_flag(self):
        return  self.was_flag

    def set_flag(self, flag:bool=False):
        self.was_flag = flag


# алгоритм дейкстры
def deixstra(init_city:str='', dists:list[CityDist]=None, cities:list[str]=None, irule:int=0):
    if init_city == '' or dists is None or cities is None:
        return 0
    lst_ans=[0,]
    cities_lst = []
    cities_lst.append(init_city)
    while len(cities_lst) < len(cities):
        next_city = ''
        min_dst = -1
        jdist = -1
        for idist in range(len(dists)):
            distance = dists[idist]
            if distance.get_flag() :
                continue
            dst_var = distance.get_distance(init_city)
            other_city = distance.get_other_city(init_city)
            if dst_var is None or other_city in cities_lst:
                continue
            elif min_dst < 0 or (min_dst > dst_var and irule == 1) or (min_dst <= dst_var and irule == 2):
                min_dst = dst_var
                next_city = other_city
                jdist = idist
        if jdist>=0 and jdist<len(dists):
            dists[jdist].set_flag(True)
            cities_lst.append(next_city)
            lst_ans[0] += min_dst
            #print("\t",min_dst, init_city, next_city)
            init_city = next_city
    lst_ans.append(' -> '.join(cities_lst))
    #print(lst_ans)
    return lst_ans

# блок решения
def code_part1(lines:list[str]=None, irule:int=1):
    if lines is None:
        return
    distances = []
    cities = set()
    for row in lines:
        if len(row) == 0:
            continue
        lst = row.split('=')
        lst2 = lst[0].strip().split(' ')
        city1 = lst2[0]
        city2 = lst2[2]
        cities.add(city1)
        cities.add(city2)
        distances.append(CityDist(lst[1], city1, city2))
    min_dist = -1
    way = ''
    print(cities)
    for city in cities:
        for dst in distances:
            dst.set_flag(False)
        distance = deixstra(city, distances, cities, irule)
        if min_dist <0 or (distance[0] < min_dist and irule == 1)  or (distance[0] > min_dist and irule == 2):
            min_dist = distance[0]
            way = distance[1]
    print("answer:", way, min_dist)


# входные данные
in_put = read_data(9)
#in_put = read_data_from_file('in.txt')

# вычисление
code_part1(in_put, 1)
code_part1(in_put, 2) #217 is low , 963 is high
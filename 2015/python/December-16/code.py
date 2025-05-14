# импорт
import json

from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file
from tools.dl import is_empty

class Aunt:
    def __init__(self, line:str=''):
        line.strip()
        pos = line.find(":")
        line1 = line[0:pos]
        self.id = line1.strip().split(" ")[1]
        line2 = line[pos+1:]
        lst = line2.strip().split(",")
        json_str = "{"
        for val in lst:
            lst2 = val.split(':')
            json_str+='"'+lst2[0].strip()+'":' + lst2[1] +","
        json_str = json_str[:-1] + "}"
        #print(json_str)
        self.dct = json.loads(json_str)
        print(self.dct)

    def compare(self, other, irule:int=1):
        if other == None:
            return 0
        ans = -1500
        cmp_state = False
        for key,val in other.dct.items():
            for key1, val1 in self.dct.items():
                if key == key1:
                    if not cmp_state:
                        ans = 0
                        cmp_state = True
                    if irule ==1:
                        ans += abs(val1 - val)
                    elif irule == 2:
                        if key == 'cats' or key == 'trees':
                            if val1 <= val:
                                ans += abs(val1 - val-1)
                        elif key == 'pomeranians' or key == 'goldfish':
                            if val1 >= val:
                                ans += abs(val1 - val-1)
                        else:
                            ans += abs(val1 - val)
                    print(ans, key, val, val1)
                    break
        return ans


    def __str__(self):
        out_str = f'i am {self.id} -{self.dct}.'
        return out_str


# вычисление
def calc_ans(lines: list[str] = None, irule: int = 0, aunt:str=''):
    ans = 0
    objects = []
    cmp_id = -1
    cmp_status = -1
    targetAunt = Aunt("Sue 0:" +aunt)
    for line in lines:
        row = line.strip()
        if is_empty(row):
            continue
        print(row)
        obj = Aunt(row)
        state = obj.compare(targetAunt, irule)
        if state <0:
            continue
        print('id: ', str(obj.id) ,",state: ", state)
        if state < cmp_status or cmp_status == -1:
            cmp_status = state
            cmp_id = obj.id
        print(obj, state)
        objects.append(obj)
    print("answer("+str(irule)+"): ", cmp_id)
# входные данные
in_put = read_data_from_serv(2015, 16)
# in_put = read_data_from_file('in.txt')

# вычисление
in_2 ="children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1"
#calc_ans(in_put, 1, in_2) # 19,257, 305,323 нет, 213 верный
calc_ans(in_put, 2, in_2) # 361, 327, 316, 213 нет, диапазон [214,326]
# 97
# 169
# 171
# 174
# 213

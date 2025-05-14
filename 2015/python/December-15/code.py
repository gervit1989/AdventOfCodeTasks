# импорт
from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file
from tools.dl import is_empty

class Ingredient:
    def __init__(self, instr:str=''):
        self.props={}
        if not is_empty(instr):
            lst = instr.split(':')
            self.name = lst[0].strip()
            lst1 = lst[1].split(',')

            for block in lst1:
                prop = block.strip().split(' ')
                self.props[prop[0]] = prop[1]

    def __str__(self):
        outstr =f"I am {self.name}. "
        for key, val in self.props.items():
            outstr += f"{key}: {val},"
        return outstr

    def get_props(self):
        return self.props

    def get_prop_val(self, key:str):
        return int(self.props[key])

class Recipe:
    def __init__(self, irule:int=0, objects=None):
        self.exclude =[]
        self.ingredients = objects
        if irule ==1:
            self.exclude.append('calories')

    def get_degree(self,amounts:list[int]=None ):
        answer = 1
        length = len(amounts)
        print(length, len(self.ingredients))
        if not( length == len(self.ingredients)):
            return answer
        props = self.ingredients[0].get_props()
        keys = props.keys()
        for key in keys:
            ans = 0
            print('key:', key)
            if key in self.exclude:
                continue
            for i in range(length):
                ans += self.ingredients[i].get_prop_val(key) * amounts[i]
            print('res1: ',ans)
            if ans < 0:
                ans = 0
            print('res: ',ans)
            answer *=ans
        return answer

# вычисление
def calc_ans(lines: list[str] = None, irule: int = 0):
    ans = 0
    objects = []
    for line in lines:
        row = line.strip()
        if is_empty(row):
            continue
        print(row)
        objects.append(Ingredient(row))

    print(*objects)
    recipe = Recipe(irule,objects)
    # генерация данных
    ans = recipe.get_degree([100, 0, 0, 0])

    print("answer("+str(irule)+"): ", ans)
# входные данные
in_put = read_data_from_serv(2015, 15)
# in_put = read_data_from_file('in.txt')

# вычисление
calc_ans(in_put, 1)
calc_ans(in_put, 2) #647 is low

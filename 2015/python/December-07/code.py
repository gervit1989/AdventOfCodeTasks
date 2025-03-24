# чтение данных
def read_data(file_name: str):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

def rule(var1:int, var2:int, rule_str:str):
    if rule_str == 'AND':
        return var1 & var2
    if rule_str == 'OR':
        return var1 | var2
    if rule_str == 'RSHIFT':
        return var1 >> var2
    if rule_str == 'LSHIFT':
        return var1 << var2
    return 0

# класс Переменная
class Var:
    # инициализация
    def __init__(self, var_name: str = '', formula: str = ''):
        self.vars = formula.split(' ')
        self.name = var_name
        self.calc_flag = False
        self.calc_val = 0

    # статус
    def get_status(self):
        return self.calc_flag

    # расчет
    def get_val(self):
        return self.calc_val

    # имя
    def get_name(self):
        return self.name

    # посчитать
    def calc(self, wires: dict = None):
        if self.calc_flag:
            return self.calc_val
        self.calc_val = -1
        if len(self.vars) == 1 and self.vars[0].isdigit():
            self.calc_flag = True
            self.calc_val = int(self.vars[0])
        elif len(self.vars) == 1:
            if self.vars[0] in wires.keys():
                self.calc_flag = True
                self.calc_val = wires[self.vars[0]]
            else:
                print('unknown var1 ', self.vars[0])
        elif len(self.vars) == 2:
            if self.vars[0] != 'NOT':
                print('unknown rule ', self.vars[0])
            var1 = self.vars[1]
            if var1 in wires.keys():
                self.calc_flag = True
                self.calc_val = 65536+(~ wires[var1])
            elif var1.isdigit():
                self.calc_flag = True
                self.calc_val = 65536+(~ int(var1))
            else:
                print('unknown var2 ', self.vars[1])
        else:
            var_names =[self.vars[0], self.vars[2]]

            vals=[]
            for var_name in var_names:
                if var_name.isdigit():
                    vals.append(int(var_name))
                elif var_name in wires.keys():
                    vals.append(wires[var_name])
            if len(vals) == 2:
                self.calc_flag = True
                self.calc_val = rule(vals[0], vals[1], self.vars[1])
            else:
                print('unknown vars')
        return self.calc_val


# часть 1
def code_part1(arg_in: str, name_of_wire: str, ch_var:str='', ch_var_val:int=0):
    # чтение данных
    in_arr = read_data(arg_in)

    # словарь
    wire_map = {}
    variables = []

    # по строкам
    for row in in_arr:
        lst = row.split(' -> ')
        if ch_var != '' and lst[1] == ch_var:
            variables.append(Var(ch_var, str(ch_var_val)))
        else:
            variables.append(Var(lst[1], lst[0]))

    while True:
        err_count = 0
        print('cycle:')
        for v in variables:
            print(v.get_name())
            answer = v.calc(wire_map)
            if v.get_status():
                wire_map[v.get_name()] = answer
            else:
                err_count += 1
        print('errs: ', err_count)
        if err_count == 0:
            break
        #break
    ans = 0
    map2 = sorted(wire_map.keys())
    for key in map2:
        print(key, wire_map[key])
        if key == name_of_wire:
            ans = wire_map[key]
    print('answer: ', ans)
    return  ans


file_name = 'input.txt'
wire_name = 'a'
ans = code_part1(file_name, wire_name)
ans = code_part1(file_name, wire_name, 'b',ans)

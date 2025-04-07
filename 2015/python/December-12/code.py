from json import JSONDecodeError

from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

def get_digit_from_str(col:None):
    digit_ans = None
    if isinstance(col, dict) or isinstance(col, list):
        return digit_ans
    #print(col)
    if isinstance(col, int):
        return col
    if col == '' or len(col) == 0:
        return digit_ans
    if col.isdigit():
        #fout.write("digit:" + col + "\n")
        return int(col)
    elif col[0] == '-' and col[1:len(col)].isdigit():
        #fout.write("digit: " + col + "\n")
        return int(col)
    else:
        # fout.write(col + "\n")
        pass
    return digit_ans

# блок решения
def code_part1(lines:list[str]=None, irule:int=1):
    if lines is None:
        return
    sum_ans = 0
    with open('code.log', 'w') as fout:
        for row in lines:
            row0 = row
            lst_data = ['{', '}', '[', ']',':', '(', ')', ',']
            lst = row.split(lst_data[0])
            #print(lst)
            for i in range(1, len(lst_data)):
                length =len(lst)
                delim = lst_data[i]
                lst2 = []
                for j in range(length):
                    string = lst[j]
                    if string == '' or len(string) == 0:
                        continue
                    lst_cur = lst[j].split(delim)
                    #print(lst_cur)
                    lst2.extend(lst_cur)
                    #break
                lst.clear()
                lst = lst2
            for col in lst:
                sum_ans+=get_digit_from_str(col)
    print("answer:", sum_ans)

import json

def get_all_pos(in_str:str=''):
    lst1=[]
    lst2=[]
    pos_start = 0
    wstr = in_str
    znak1 = '{'
    znak2 = '}'
    while True:
        # if pos_start<0:
        #     pos1 = wstr.find(znak1)
        #     pos2 = wstr.find(znak2)
        # else:
        pos1 = wstr.find(znak1, pos_start)
        pos2 = wstr.find(znak2, pos_start)
        print(pos_start, pos1, pos2, "\nlst1:", lst1, "\nlst2:",lst2)
        if pos1>pos_start or pos2 > pos_start:
            wstr2 = wstr[pos1:pos2+1]
            lst1.append(wstr[pos_start:pos1])
            if wstr2.count(znak1, 1) == 0:
                pos_start = pos2+1
                lst2.append(wstr2)
            else:
                icount1 = 0
                pos_start = pos2+1
                while True:
                    pos3 = wstr.find(znak2, pos_start)
                    wstr3 = wstr[pos1:pos3+1]
                    ival1 =wstr3.count(znak1)
                    ival2 =wstr3.count(znak2)
                    print(wstr3, pos_start, pos3, ival1, ival2)
                    pos_start = pos3+1
                    if  ival1 == ival2:
                        wstr2 = wstr[pos1:pos3+1]
                        lst2.append(wstr2)
                        break
        else:
            lst1.append(wstr[pos_start:])
            break
    lst_ans = []
    lst_ans.append(lst1)
    lst_ans.append(lst2)
    return lst_ans

def block_list(in_str:str):
    sum_ans = 0
    if in_str.count('{'):
        lst_json = get_all_pos(in_str)
        print(lst_json)
        sum_ans += block_list(lst_json[0])
        for var in lst_json[1]:
            sum_ans += block_json(var)
    else:
        lst = str.split(',')
        for var in lst:
            sum_ans+=get_digit_from_str(var)
    return sum_ans

def block_list2(in_data, ilvl):
    sum_ans = 0
    for var in in_data:
        state = get_digit_from_str(var)
        if state is None:
            if isinstance(var, list):
                sum_ans += block_list2(var, ilvl+1)
            elif isinstance(var,dict):
                sum_ans += block_json(var, ilvl+1)
        else:
            sum_ans+= state
    return sum_ans

def block_json(in_str1, ilvl):
    sum_ans = 0
    try:
        obj = None
        if isinstance(in_str1, dict):
            obj = json.dumps(in_str1)
        else:
            obj = in_str1
        in_str = in_str1
        if ilvl < 1:
            print("in: ", in_str)

        jdata = json.loads(obj)
        if 'red' not in jdata.values():
            for key, val in jdata.items():
                if ilvl < 1:
                    print("key= ", key, "\nval=", val)
                if isinstance(val, list):
                    if ilvl < 1:
                        print('block: ',sum_ans)
                    sum_ans +=block_list2(val, ilvl+1)
                    if ilvl < 1:
                        print(sum_ans)
                elif isinstance(val, dict):
                    if ilvl < 1:
                        print('json: ',sum_ans)
                    sum_ans +=block_json(val, ilvl+1)
                    if ilvl < 1:
                        print(sum_ans)
                else:
                    state = get_digit_from_str(val)
                    if state is not None:
                        if ilvl <1:
                            print('var: ',sum_ans)
                        sum_ans += state
                        if ilvl < 1:
                            print(sum_ans)
        elif ilvl <1:
            print('red str')
    except json.JSONDecodeError as e:
        print("block end", e.msg)
    return sum_ans


def code_2(lines:list[str]=None):
    sum_ans = 0
    for row in lines:
        print(row)
        if len(row) == 0 or row == '':
            continue
        sum_ans +=block_json(row, 0)

    print("answer:", sum_ans)



# входные данные
in_put = read_data_from_serv(2015, 12)
#in_put = read_data_from_file('in.txt')

# вычисление
#code_part1(in_put, 1) # 197248 is too high, 12328 is too low, 119214 high
#code_part1(in_put, 2)
code_2(in_put)
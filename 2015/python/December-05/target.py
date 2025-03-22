# чтение данных
def read_data(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data


# Количество букв из списка
def get_count_of_letters_in_lst(line_str: str, lst: list = None):
    icount = 0
    for letter in lst:
        icount += line_str.count(letter)
    return icount

def rule1(line_str:str):
    letter_count = get_count_of_letters_in_lst(line_str, list('aeiou'))
    case2 = False
    case3 = True
    if letter_count >= 3:
        alphabets = []
        for i in range(97, 123):
            alphabets.append(chr(i))
        alphabet_size = len(alphabets)
        for i in range(alphabet_size):
            str_init = alphabets[i]
            str1 = str_init + str_init
            if line_str.count(str1):
                case2 = True
        lst_not_allowed = ['ab', 'cd', 'pq', 'xy']
        for comb in lst_not_allowed:
            if line_str.count(comb):
                case3 = False
        if case2 and case3:
            return 1
    return 0

def rule2(line_str:str):
    alphabets = []
    for i in range(97, 123):
        alphabets.append(chr(i))
    alphabet_size = len(alphabets)
    case1 = False
    case2 = False
    for letter in alphabets:
        if line_str.count(letter)>=2:
            pos2 = 0
            while True:
                pos1 = line_str.find(letter, pos2)
                pos2 = line_str.find(letter, pos1+1)
                #print(pos1, pos2)
                if pos2 == pos1+2:
                    case2 = True
                    break
                if pos2 == -1:
                    break
        for letter2 in alphabets:
            comb = letter+letter2
            if line_str.count(comb)>=2:
                pos1l = line_str.find(letter)
                pos2l = line_str.find(letter, pos1l+2)
                if pos2l >=0:
                    case1 = True
    #print(case1, case2)
    if case1 and case2:
        return 1
    return 0

# часть 1
def part1_of_task(arg_name: str, num_rule:int):
    in_arr = read_data(arg_name)
    sum_ans = 0
    for row in in_arr:
        lst1 = row.split('=')
        answer = 0
        if len(lst1) > 1:
            answer = int(lst1[1])
        answer_var = 0
        line_var = lst1[0]
        if num_rule == 1:
            answer_var = rule1(line_var)
        elif num_rule == 2:
            answer_var = rule2(line_var)
        #print(letter_count, case2, case3)
        print('on row ', answer_var, answer_var - answer)
        sum_ans += answer_var - answer
    print('ans of part1:= ', sum_ans)


file_name = 'input.txt'
part1_of_task(file_name, 1)
part1_of_task(file_name, 2)

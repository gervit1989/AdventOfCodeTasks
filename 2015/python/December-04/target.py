import hashlib

# чтение данных
def read_data(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

# часть 1
def part1_of_task(arg_name:str, arg_str:str):
    in_arr = read_data(arg_name)
    sum_ans = 0
    for row in in_arr:
        lst1 = row.split('=')
        answer = 0
        if len(lst1) > 1:
            answer = int(lst1[1])
        #ival = 10**(len(lst1[0])-1)
        num_val = 0
        while True:
            str_data1 = str(lst1[0]) + str(num_val)
            res = hashlib.md5(str_data1.encode()).hexdigest()
            #print("res: ", ival, str_data1, res)
            if res.startswith(arg_str):
                break
            num_val+=1
        answ = num_val
        print('on row ', answ, answ - answer)
        sum_ans += answ - answer
    print('ans of part1:= ', sum_ans)


name_arg = 'in.txt'
str_find = '00000'
part1_of_task(name_arg, str_find)
str_find = '000000'
part1_of_task(name_arg, str_find)
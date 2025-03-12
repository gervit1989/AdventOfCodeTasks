# чтение данных
def read_data(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

# часть 1
def part1_of_task():
    in_arr = read_data('input.txt')
    for row in in_arr:
        lst = list(row)
        floor_id=0
        for letter in lst:
            if letter == '(':
                floor_id+=1
            elif letter == ')':
                floor_id-=1
        print('res for row ', row[:25], " is : ",floor_id)

# часть 1
def part2_of_task():
    in_arr = read_data('input.txt')
    for row in in_arr:
        lst = list(row)
        floor_id=0
        pos = 0
        fpos = 0
        flag_found = False
        print('len:', len(lst))
        for letter in lst:
            if letter == '(':
                floor_id+=1
            elif letter == ')':
                floor_id-=1
            if floor_id == -1 and not flag_found:
                fpos = pos+1
                print('pos: ', pos)
                flag_found = True
            pos+=1

        print('res for row ', row[:25], " is : ",fpos)


# часть 1
part1_of_task()
# часть 2
part2_of_task()
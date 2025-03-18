# чтение данных
def read_data(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

# часть 1
def part1_of_task(name_arg):
    in_arr = read_data(name_arg)
    sum_ans = 0
    for row in in_arr:
        lst1 = row.split('=')
        lst = lst1[0].split('x')
        ans = 0
        if len(lst1) > 1:
            ans = int(lst1[1])
        #print(lst, ans)
        ans1 = 0
        ans2 = 0
        lstd = [float(x) for x in lst]
        length = lstd[0]
        width = lstd[1]
        height = lstd[2]
        ans1 = 2 * length * width + 2 * width * height + 2 * height * length
        lstd.sort()
        ans2 = lstd[0] * lstd[1]
        sum_ans += ans1 + ans2
    print("ans: ", sum_ans)


# часть 2
def part2_of_task(name_arg: None):
    in_arr = read_data(name_arg)
    sum_ans = 0
    for row in in_arr:
        lst1 = row.split('=')
        lst = lst1[0].split('x')
        lstd = [float(x) for x in lst]
        length = lstd[0]
        width = lstd[1]
        height = lstd[2]
        lstd.sort()
        ans1 = 2 * lstd[0] + 2 * lstd[1]
        ans2 = length * width * height
        sum_ans += ans1 + ans2
    print("ans2: ", sum_ans)

sname = 'input.txt'
part1_of_task(sname)
part2_of_task(sname)
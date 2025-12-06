
def read_data(address):
    in_data = []
    with open(address, "r") as fin:
        in_data = [tuple(map(int,row.strip().split(','))) for row in fin.readlines()]
    return in_data

addr = 'in1.txt'
inp = read_data(addr)
#print(*inp)
in_pos = (0,0)
lens = (71,71)
count_of = 1024
if addr == 'in1.txt':
    lens = (7,7)
    count_of = 12
for i in range(lens[0]):
    str_val =''
    for j in range(lens[1]):
        is_found = False
        for k in range(count_of):
            if j == inp[k][0] and i == inp[k][1]:
                is_found =True
                break
        str_val += '#' if is_found else '.'
    print(str_val)



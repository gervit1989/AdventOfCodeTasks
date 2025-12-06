def read_data(address):
    in_data = []
    with open(address, "r") as fin:
        in_data = [row.strip().split(':') for row in fin.readlines() if len(row.strip())]
    return in_data

addr = 'in.txt'
inp = read_data(addr)
print(*inp)
mapx = {}
program_lst = []
prog_str = ''
for i in range(len(inp)):
    if i == 3:
        prog_str = inp[i][1].strip()
        program_lst = list(map(int, prog_str.split(",")))
    else:
        key_new = inp[i][0].split(' ')[1]
        mapx[key_new] = int(inp[i][1].strip())
print(mapx.items())
print(program_lst)
mapx2 = {4:'A', 5:'B', 6:'C'}
out_str=''
i=0
len1 =len(program_lst)-1
while i<len1:
    oper = program_lst[i]
    operand = program_lst[i+1]
    literal_operand = operand
    if operand in mapx2.keys():
        operand = mapx[mapx2[operand]]
    print('i: ',i, ' oper: ',oper, "var: ", operand, ' out: ', out_str, " map: ", mapx)
    if oper == 0 or oper == 7:
        mapx['A' if oper == 0 else 'C'] = mapx['A']//(2**operand)
    elif oper == 1:
        mapx['B'] ^= literal_operand
    elif oper == 2:
        mapx['B'] = operand %8
    elif oper == 3 and mapx['A'] != 0:
        i=literal_operand
        continue
    elif oper == 4:
        mapx['B'] ^= mapx['C']
    elif oper == 5:
        out_str += str(operand%8) + ','
    elif oper == 6:
        mapx['B'] = mapx['A']//(2**operand)
    i+=2
print(mapx)
print(out_str[0:-1])
res_str=[out_str[i] for i in range(len(out_str)-1) if i%2==0]
res_str = ''.join(res_str)
print(int((res_str)))
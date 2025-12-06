def read_data(address):
    in_data = []
    with open(address, "r") as fin:
        in_data = [row.strip().split(':') for row in fin.readlines() if len(row.strip())]
    return in_data

mapx2 = {4:'A', 5:'B', 6:'C'}

def run_sol(val_a, map_, prog_lst):
    mapx = {}
    for key, val in map_.items():
        mapx[key] = val
    mapx['A'] = val_a
    out_str=''
    i=0
    print(val_a)
    len1 =len(prog_lst)-1
    while i<len1:
        oper = prog_lst[i]
        operand = prog_lst[i+1]
        literal_operand = operand
        if operand in mapx2.keys():
            operand = mapx[mapx2[operand]]
        #print('i: ',i, ' oper: ',oper, "var: ", operand, ' out: ', out_str, " map: ", mapx)
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
    return out_str


addr = 'in.txt'
inp = read_data(addr)
print(*inp)
mapx_ = {}
mapx_orig= {}
program_lst = []
prog_str = ''
for i in range(len(inp)):
    if i == 3:
        prog_str = inp[i][1].strip()
        program_lst = list(map(int, prog_str.split(",")))
    else:
        key_new = inp[i][0].split(' ')[1]
        mapx_[key_new] = int(inp[i][1].strip())
        mapx_orig[key_new] = mapx_[key_new]
print(mapx_orig.items())
print(program_lst)
ans = 0
ans_lst=[]
for i in range(len(prog_str)+1, 0, -1):
    z = 10**i
    out_string = run_sol(z, mapx_orig, program_lst)
    print(z, out_string, len(out_string)-1, len(prog_str))
    if len(out_string)-1 < len(prog_str):
        out_string = out_string[0:-1]
        print(out_string, prog_str)
        if out_string == prog_str:
            ans_lst.append(z)
        z1 = 10**(i+2)#100000000000000
                      #164546529292221
        shift = 10**i
        print(z1, shift)
        shift1 = 0
        #while True:
        step = (z1-shift)//100
        z2 =0
        z3 = 0
        for q in range(z1, z,-step):
            out_string = run_sol(q, mapx_orig, program_lst)
            print(q, out_string, len(out_string)-1, len(prog_str))
            if len(out_string)-1 == len(prog_str):
                if z2 == 0 and z3 == 0:
                    z2 = q
                    z3 = q
                if q < z2:
                    z2 = q
                out_string = out_string[0:-1]
                print(out_string, prog_str)
                if out_string == prog_str:
                    ans_lst.append(q)
        for q in range(z3, z2,-1):

            out_string = run_sol(q, mapx_orig, program_lst)
            print(q, out_string, len(out_string)-1, len(prog_str))
            if len(out_string)-1 == len(prog_str):
                out_string = out_string[0:-1]
                print(out_string, prog_str)
                if out_string == prog_str:
                    ans_lst.append(q)
                    break
        break

# for ind in range(len(program_lst)-1, 0, -1):
#     res = program_lst[ind] # результат операции 5
#     for i in range(8):
#         pass


ans = min(ans_lst)
print("ans: ", ans)
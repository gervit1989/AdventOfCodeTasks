
def read_data():
    in_data = []
    with open("in1.txt", "r") as fin:
        in_data = list(fin.read().strip())
    return in_data

line = read_data()
print(*line)

pos = 0
id_var = 0
out_data=[]
for elem in line:
    symb = ('.' if pos %2 else str(id_var))
    for i in range(int(elem)):
        out_data.append(symb)
    if pos %2 == 0:
        id_var += 1
    pos+=1
print(out_data)
pos = len(out_data)-1
bound0 = int(line[0])
while True:
    if pos <= bound0:
        break
    while True:
        if out_data[pos].isdigit():
            break
        if pos <= bound0:
            break
        pos-=1
    if pos <= bound0:
        break
    ind_var = out_data.index('.')
    if ind_var <pos:
        out_data[ind_var], out_data[pos] = out_data[pos],'.'
    else:
        break
    #print(*out_data)
    pos -=1
    print(pos)
#out_data = list("0099811188827773336446555566..............")
sum_var = 0
for i in range(len(out_data)):
    if not out_data[i].isdigit():
        break
    sum_var += i *int(out_data[i])
print("ans: ", sum_var)

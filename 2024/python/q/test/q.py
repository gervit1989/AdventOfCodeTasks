
def read_data(address):
    with open(address, "r") as fin:
        in_data = [row for row in fin.readlines()]
    return in_data

in_data = read_data('in.txt')
iLine = 0
inum=1
flag_h = False
for line in in_data:
    lst = list(line)
    ix = 0
    for lt in lst:
        if lt=='H':
            print(inum, lt, iLine, ix)
            #print(iLine, ix)
            if inum == 157:
                #print(iLine, ix)
                flag_h = True
                break
            inum +=1
        ix+=1
    iLine +=1
    if flag_h:
        break
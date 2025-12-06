# чтение данных
def read_data(file_name: str, q:bool):
    in_data = None
    with open(file_name, 'r') as fin:
        if q==True:
            in_data = [row.strip() for row in fin.readlines()]
        else:
            in_data = [row for row in fin.readlines()]
    return in_data

def part1(rule:int):
    inarr=read_data('in.txt', True)
    cntvl=0
    m=len(inarr)
    matrix = []
    n = -1
    for line in inarr:
        symbols = line.split(' ')
        nsymb=[]
        for symbol in symbols:
            if len(symbol)>0:
                nsymb.append(symbol)
        matrix.append(nsymb)
        n = len(nsymb)
        print(n)
    for j in range(0,n):
        cntvlx=1
        sgnvl=matrix[m-1][j].strip()
        for i in range(m-1):
            elm=int(matrix[i][j].strip())
            if  sgnvl=='*':
                cntvlx*=elm
            elif sgnvl=='+':
                if i==0:
                    cntvlx=0
                cntvlx+=elm
        #print(cntvlx)
        cntvl+=cntvlx
    print('ans by rule '+str(rule)+': ', cntvl)

def part2(rule:int):
    inarr=read_data('in.txt', False)
    symbols = inarr[-1].strip().split(' ')
    nsymb=[]
    for symbol in symbols:
        if len(symbol)>0:
            nsymb.append(symbol)
    matrix=[]
    m=len(inarr)
    n=0
    for i in range(m-1):
        smbls=list(inarr[i])
        matrix.append(smbls[:-1])
        n= max(n, len(smbls)-1)
    for i in range(m - 1):
        curlen=len(matrix[i])
        for j in range(curlen, n):
            matrix[i].append('')
    lst=[]
    ind_oper = len(nsymb)-1
    cntvl=0
    for j in range(n-1,-1,-1):
        cntvlx=0
        lst2=[]
        for i in range(m-1):
            elm=matrix[i][j]
            if len(elm)>0 and not(elm==' '):
                lst2.append(int(elm))
        #print(spcnt)
        if len(lst2)>0:
            for k in range(len(lst2)):
                cntvlx+=lst2[k]*(10**(len(lst2)-1-k))
        if cntvlx!=0:
            print(cntvlx)
            lst.append(cntvlx)
        if len(lst2)==0 or j==0:
            print('q')
            if nsymb[ind_oper]=='*':
                cntvlx=1
                for x in lst:
                    cntvlx*=x
            elif nsymb[ind_oper]=='+':
                cntvlx=sum(lst)
            ind_oper-=1
            print('col: ', cntvlx)
            cntvl += cntvlx
            lst.clear()

    print('ans by rule ' + str(rule) + ': ', cntvl)

# part1(1)
part2(2)
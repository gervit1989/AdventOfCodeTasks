# чтение данных
def read_data(file_name: str):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data

def get_is_right_cell_(i:int, j:int, arr, k:int, szes):
    vl=0
    for i1 in range(i-1,i+2):
        for j1 in range(j - 1, j + 2):
            if i1 <0 or j1<0 or i1>=szes[0] or j1>=szes[1] or (i1==i and j1==j):
                continue
            if arr[i1][j1]=='@':
                vl+=1
    print(vl)
    if vl < k:
        return True
    return False

in_arr = read_data('in.txt')
matrix = []
n=-1
m = len(in_arr)
for line in in_arr:
    symbols = list(line)
    matrix.append(symbols)
    n = len(symbols)
ansvl=0
for i in range(m):
    for j in range(n):
        if matrix[i][j]=='@':
            if get_is_right_cell_(i,j, matrix, 4,(m,n)):
                print(i,j, matrix[i][j], 1)
                ansvl+=1
                continue
        print(i, j, matrix[i][j], 0)
print(ansvl)
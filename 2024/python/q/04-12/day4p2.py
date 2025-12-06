from tkinter.filedialog import dialogstates
from turtledemo.clock import datum

is_used = 0
used_indexes = []

def is_valid(grid, y, x):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def check_xmas_3(grid, x, y):
    ans = 0
    try:
        diag1 = grid[x-1][y-1]+grid[x+1][y+1]
        diag2 = grid[x-1][y+1]+grid[x+1][y-1]
        print(diag1, diag2)
        data = ["MS", "SM"]
        if (diag1 in data and diag2 in data):
            ans = 1
            print((x,y), diag1, diag2)
            print((grid[x-1][y-1], "*",grid[x-1][y+1]), ('*', 'A','*'), (grid[x+1][y-1], "*",grid[x+1][y+1]), sep="\n")
    except:
        print("err")
        ans = 0
    return ans

lines = []
with open("in.txt", "r") as file:
    lines = file.readlines()
print(lines)
matrix = []
n_min = -1
n_max = -1
m = len(lines)
for line in lines:
    symbols = list(line)
    matrix.append(symbols)
    n = len(symbols)
    if n<=0:
        continue
    if n_min == -1 or n_min>n:
        n_min = n
    if n_max == -1 or n_max>n:
        n_max = n
print(m, n_min, n_max)
count_n = n_max
if  not (n_max == n_min):
    print("err in counts")
end_lst = (m, count_n)
sum_var = 0
for i in range(1,m-1):
    for j in range(1,count_n-1):
        if matrix[i][j] == "A":
            print(i,j)
            res =check_xmas_3(matrix, i, j)
            if res:
                #print("zz")
                sum_var += res
        #sum_var +=check_pos(matrix, (i, j), find_txt, end_lst)
        #break
    #break
print(sum_var)
if is_used:
    print(used_indexes)
    for i in range(m):
        for j in range(count_n):
            if used_indexes.count((i,j)) == 0:
                print(".", end="")
            else:
                print(matrix[i][j], end="")
        print("\n")
#2534 is high
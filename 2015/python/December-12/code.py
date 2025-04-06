from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

# блок решения
def code_part1(lines:list[str]=None, irule:int=1):
    if lines is None:
        return
    sum_ans = 0
    with open('code.log', 'w') as fout:
        for row in lines:
            row0 = row
            lst_data = ['{', '}', '[', ']',':', '(', ')', ',']
            lst = row.split(lst_data[0])
            #print(lst)
            for i in range(1, len(lst_data)):
                length =len(lst)
                delim = lst_data[i]
                lst2 = []
                for j in range(length):
                    string = lst[j]
                    if string == '' or len(string) == 0:
                        continue
                    lst_cur = lst[j].split(delim)
                    #print(lst_cur)
                    lst2.extend(lst_cur)
                    #break
                lst.clear()
                lst = lst2
            for col in lst:
                if col == '' or len(col) == 0:
                    continue
                if col.isdigit():
                    fout.write("digit:" + col + "\n")
                    sum_ans += int(col)
                elif col[0] == '-' and col[1:len(col)].isdigit():
                    fout.write("digit: " + col + "\n")
                    sum_ans += int(col)
                else:
                    fout.write(col + "\n")
    print("answer:", sum_ans)


# входные данные
in_put = read_data_from_serv(2015, 12)
#in_put = read_data_from_file('in.txt')

# вычисление
code_part1(in_put, 1) # 197248 is too high, 12328 is too low, 119214 high
#code_part1(in_put, 2)
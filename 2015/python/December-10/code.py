from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

# блок решения
def code_part1(lines:list[str]=None, irule:int=1, try_count: int=0):
    if lines is None:
        return
    if try_count == 0:
        return
    answer = 0
    for row in lines:
        if len(row) == 0:
            continue
        print('new line')
        row0 = row
        for itry in range(try_count):
            row1 = []
            pos = 0
            length = len(row0)
            while True:
                icount = 1
                letter = row0[pos]
                #print("ch letter ", letter, pos)
                if pos +1 == length:
                    row1.append(str(icount) + letter)
                    break
                else:
                    posinit = pos
                    for i in range(pos+1, length):
                        letter2 = row0[i]
                        #print("next:",letter2, pos)
                        if letter2 == letter:
                            icount+=1
                        else:
                            pos = i
                            row1.append(str(icount) + letter)
                            break
                    #print(pos, posinit, icount, length)
                    if posinit + icount == length:
                        row1.append(str(icount) + letter)
                        break
            row0 = ''.join(row1)
            print("try ", itry, ": ", len(row0))
        answer = len(row0)
    print("answer:", answer)


# входные данные
in_put = ['1', '11', '21', '1211', '111221']#,
in_put = ['1113122113']#read_data_from_serv(2015,10)
#in_put = read_data_from_file('in.txt')

# вычисление
code_part1(in_put, 1, 50)
#code_part1(in_put, 2, 50) #217 is low , 963 is high
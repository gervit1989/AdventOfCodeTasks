from tools.dl import download_input

# чтение данных
def read_data(day: int):
    in_str = download_input(2015, 8)
    in_data = in_str.split('\n')
    for i in range(len(in_data)):
        in_data[i] = in_data[i].strip()
    return in_data

def answer1(row:str=''):
    length = len(row)
    ans2 = 0
    i=0
    while i < length:
        letter = row[i]
        if letter.isdigit() or letter.isalpha():
            ans2+=1
            i+=1
        else:
            print(i, letter)
            if letter =='\\':
                letter = row[i+1]
                if letter == 'x':
                    ans2 += 1
                    i = i+4
                elif letter =='"' or letter == '\\':
                    ans2+=1
                    i+=2
            else:
                i+=1
    return length -ans2
# ответ 2
def answer2(row:str=''):
    length = len(row)
    row2 = '"\\"'
    i=1
    while i < length-1:
        letter = row[i]
        if letter.isdigit() or letter.isalpha():
            row2 = row2 + letter
            i+=1
        else:
            if letter =='\\':
                letter = row[i+1]
                if letter == 'x':
                    row2 = row2+"\\\\x"
                    i+=2
                elif letter =='"':
                    row2 = row2+'\\\\\\"'
                    i+=2
                elif letter =='\\':
                    row2 = row2+'\\\\\\\\'
                    i+=2
            else:
                i+=1
    row2 = row2 + '\\""'
    ans2 = len(row2)
    return ans2-length

# часть 1
def code_part1(lines:list[str]=None, irule:int=0):
    answer = 0
    for row in lines:
        if row == '' or len(row) == 0:
            continue
        if irule == 1:
            answer += answer1(row)
        elif irule == 2:
            answer += answer2(row)
    print(answer)

in_put = read_data(8)
code_part1(in_put, 1)
code_part1(in_put, 2)
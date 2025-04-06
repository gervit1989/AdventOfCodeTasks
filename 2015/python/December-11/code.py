from tools.dl import read_data_from_serv
from tools.dl import read_data_from_file

def get_letters():
    lst = ['o', 'i', 'l']
    return lst

def is_in_rule(s_in:str='',irule:int=0, stream=None, lst_ab=None):
    answ = True
    if irule == 2:
        icount = 0
        for letter in lst_ab[irule-1]:
            lic = s_in.count(letter)
            #print('rule 1:', letter, lic)
            icount += lic
            if icount > 0:
                print(s_in, letter)
        answ = icount > 0
    elif irule == 1:
        #print('xxxx')
        lst = get_letters()
        #print(lst)
        for letter in lst:
            countx_var = s_in.count(letter)
            #print(countx_var, letter)
            if s_in.count(letter):
                return False
    elif irule == 3:
        answ = False
        count_var = 0
        pos1 = -1
        for letter in lst_ab[irule-1]:
            icountx = s_in.count(letter)
            pos_var = s_in.find(letter)
            #print(str(pos_var), "QQ", str(pos1))
            str_var ="pos0x: " + str(pos1) + ", " + letter + ", " + str(icountx) + ", " + str(pos_var) + ", " + str(count_var) + "\n"
            #print(str_var)
            #print(letter, s_in, icountx)
            if pos_var>=0:
                icountx = 1
                # print(letter, s_in, icountx, "!")
                #stream.write("pos0: "+ str(pos1)+ ", "+letter+ ", "+str(icountx)+ ", "+str(count_var)+"\n")
                if count_var == 0:
                    pos1 = pos_var
                    count_var +=1
                    #stream.write("pos1: "+ str(pos1)+ ", "+letter+ "\n")
                elif count_var == 1:
                    pos3 = pos_var
                    pos2 = s_in.find(letter, pos1+2)
                    #stream.write("pos2: "+ str(pos1)+ ", "+ str(pos2)+ ", "+ str(pos3)+ ", "+ letter+ "\n")
                    if pos2 >= pos1+2:
                        return True
                    elif pos3 +2 <= pos1:
                        return True
    return answ

def increase_str(s_in:str=''):
    answ =''
    lst = []
    length = len(s_in)
    ipos = 0
    while True:
        letter = s_in[-ipos-1]
        num = ord(letter)
        #print(letter, num)
        if num + 1 == 123:
            lst.append( chr(97))
            ipos +=1
        else:
            lst.append( chr(num+1))
            lst.append( s_in[0:length - ipos-1])
            break
    answ =''.join(lst[::-1])
    return answ

def change_to_right(s_in:str=''):
    #print('x', s_in)
    if not is_in_rule(s_in,1):
        #print('t')
        pos_lst = []
        lst = get_letters()
        for letter in lst:
            pos_var = s_in.find(letter)
            if pos_var >=0:
                pos_lst.append(pos_var)
        if len(pos_lst)>0:
            len1=len(s_in)
            len2 =len1 - min(pos_lst)-1
            s_part1 = s_in[0:min(pos_lst)+1]
            #print(s_part1)
            s_mod = increase_str(s_part1) + 'a' *len2
            #print(s_mod)
            return change_to_right(s_mod)
    return s_in

# блок решения
def code_part1(lines:list[str]=None, irule:int=1):
    if lines is None:
        return
    if irule ==1:
        lst_ab = []
        lst0 = []
        for i in range(97, 123):
            lst0.append(chr(i))
        lst_ab.append(lst0)
        lst_ab3 = []
        for i in range(97, 121):
            var =chr(i) + chr(i + 1) + chr(i + 2)
            lst_ab3.append(var)
        lst_ab.append(lst_ab3)
        lst2 = []
        for i in range(97, 123):
            lst2.append(chr(i) + chr(i))
        lst_ab.append(lst2)
        print(lst_ab)

        with open('code.log', 'w') as fout:
            row_in = lines[0]
            row_in = change_to_right(row_in)
            while True:
                fout.write("\nin: " + row_in)
                row_out = increase_str(row_in)
                fout.write(", out: "+ row_out)
                flag = True
                jrule =1
                while True:
                    if not is_in_rule(row_out,jrule, fout, lst_ab):
                        fout.write("\trule " +str(jrule) +" No")
                        if jrule == 1:
                            fout.write("\nin: " + row_out)
                            row_out = change_to_right(row_out)
                            fout.write(", out: " + row_out + "\trule " +str(jrule) +" Ok")
                            jrule=1
                        else:
                            flag = False
                            break
                    else:
                        fout.write("\trule " +str(jrule) +" Ok")
                    jrule+=1
                    if jrule>=4:
                        break
                row_in = row_out
                if flag:
                    break
                #break

    print("answer:", row_in)
    return row_in


print(increase_str('yzz'))

# входные данные
in_put = ['hijklmmn', 'abbceffg', '21', '1211', '111221']#,
in_put0 = ['abcdefgh']
in_put1 = ['ghijklmn']
in_put = ['vzbxkghb']#read_data_from_serv(11)
#in_put = read_data_from_file('in.txt')

# вычисление
out0 = code_part1(in_put, 1)
out1 = code_part1([out0], 1)
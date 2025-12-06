def multiply_from_str(data):
    prod = 0
    #multipliers_str = None
    multipliers = []
    #print("input: ", data)
    try:
        var_index_2 = data.find(")")
        #print("q", var_index_2, data)
        if var_index_2 != -1:
            part = data[:var_index_2]
            multipliers_str = tuple(part.split(","))
            ch =''
            for symb in part:
                if symb.isdigit():
                    ch += symb
                elif symb == ",":
                    if ch.isdigit():
                        var_val = int(ch)
                        multipliers.append(var_val)
                    ch=''
                else:
                    ch = ''
                    break
            if ch.isdigit():
                multipliers.append(int(ch))
    except Exception as e:
        print(f"some err {type(e)}, {e}")
    finally:
        if multipliers:
            #print("len:=",len(multipliers))
            if len(multipliers)==2:
                prod = int(multipliers[0])*int(multipliers[1])
    if prod > 0:
        print(multipliers[0], multipliers[1])
        #print(f"prod({multipliers}):=",prod)
    return prod

content = None
with open("input.txt", "r") as file:
    content = file.read()
#print(content)
#content = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
sum_var = 0
find_txt = ["mul(","don't()","do()"]
try:
    var_index = -1
    var_pos = -1
    for i in range(len(find_txt)):
        var_index_f = content.find(find_txt[i])
        if var_index_f<var_index or var_index == -1:
            var_index = var_index_f
            var_pos = i
    print(var_index)
    is_enabled = 1
    if var_pos == 1:
        is_enabled = 0
    vars = []
    while var_index != -1:
        shift =len(find_txt[var_pos])
        print(shift)
        content = content[var_index + shift:]
        var_index = -1
        var_pos = -1
        for i in range(len(find_txt)):
            var_index_f = content.find(find_txt[i])
            if var_index_f < var_index or var_index == -1:
                var_index = var_index_f
                var_pos = i
        print(var_pos, var_index)
        if var_pos == 1:
            is_enabled = 0
        if var_pos == 2:
            is_enabled = 1
        if var_index != -1 and var_pos == 0:
            part_of_str = content[:var_index]
            #print(part_of_str)
            if not is_enabled:
                continue
            tmp_var =multiply_from_str(part_of_str)
            if tmp_var > 0:
                sum_var += tmp_var
                vars.append((tmp_var,part_of_str))
        elif var_pos == 0:
            #print(content)
            part_of_str = content

            tmp_var =multiply_from_str(part_of_str)
            if tmp_var > 0:
                sum_var += tmp_var
                vars.append((tmp_var,content))
            break
except ValueError:
    print(f"no str {find_txt}")
finally:
    print("End")
print(sum_var)
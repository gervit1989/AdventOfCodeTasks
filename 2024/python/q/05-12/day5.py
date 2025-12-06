
def is_right_rule(update, list):
    rules = []
    for num in update:
        for num1 in update:
            if num1 == num:
                continue
            #print(num, num1)
            if list.count([str(num), str(num1)]) != 0:
                if rules.count([num, num1]) ==0:
                    rules.append([num, num1])
                    #print("1")
            if list.count([str(num1), str(num)]) != 0:
                if rules.count([num1, num]) ==0:
                    rules.append([num1, num])
                    #print("1")
    #print("x")
    #print(*rules, sep="\n")
    rules_is_done = True
    for rule in rules:
        pos1 = update.index((rule[0]))
        pos2 = update.index((rule[1]))
        #print(rule, pos1, pos2)
        if pos1 > pos2:
            rules_is_done = False
            break
    return rules_is_done

def fix_update(update, list):
    rules = []
    for num in update:
        for num1 in update:
            if num1 == num:
                continue
            #print(num, num1)
            if list.count([str(num), str(num1)]) != 0:
                if rules.count([num, num1]) ==0:
                    rules.append([num, num1])
                    #print("1")
            if list.count([str(num1), str(num)]) != 0:
                if rules.count([num1, num]) ==0:
                    rules.append([num1, num])
                    #print("1")
    rules2 = []
    new_upd = update
    while True:
        is_right =True
        for rule in rules:
            pos1 = update.index((rule[0]))
            pos2 = update.index((rule[1]))
            #print(rule, pos1, pos2)
            if pos1 > pos2:
                is_right = False
                new_upd[pos1] = rule[1]
                new_upd[pos2] = rule[0]
        if is_right:
            break
    return new_upd

lines = []
lpart1 = []
lpart2 = []
flag = False
with open("in.txt", "r") as file:
    lines = file.readlines()
for elem in lines:
    str_var = elem.strip()
    if len(str_var) == 0:
        flag = True
        continue
    if flag:
        lpart2.append(str_var.split(","))
    else:
        lpart1.append(str_var.split("|"))
#print(*lpart1, sep ="\n")
#print("xxx")
#print(*lpart2, sep ="\n")

sum_mid_values = 0
list_rights = []
sum_mid_values2 = 0
list_fixed = []

for elem in lpart2:
    print(elem)
    res = is_right_rule(elem, lpart1)
    if res:
        list_rights.append(elem)
    else:
        var =fix_update(elem, lpart1)
        list_fixed.append(var)
        print(is_right_rule(var, lpart1))
    #break

#list_rights.append((75,47,61,53,29))
#list_rights.append ((97,61,53,29,13))
#list_rights.append((75,29,13))
print("final")
for elem in list_rights:
    print(elem)
    if len(elem)== 0:
        continue
    val_mid = elem[len(elem)//2]
    print(val_mid)
    sum_mid_values+= int(val_mid)
print("ans: ",sum_mid_values)
for elem in list_fixed:
    print(elem)
    if len(elem)== 0:
        continue
    val_mid = elem[len(elem)//2]
    print(val_mid)
    sum_mid_values2+= int(val_mid)
print("ans2: ",sum_mid_values2)#4924 is low

def lst_to_int(lstvl):
    vl="".join(lstvl)
    return int(vl)

def get_max_start(lst:list):
    maxvl=lst[0]
    imaxvl=0
    for i in range(1, len(lst)):
        if lst[i]>maxvl:
            maxvl = lst[i]
            imaxvl=i
    return maxvl,imaxvl

def get_max_block(lstvl, sze:int):
    lsteq=[]
    lenvl=len(lstvl)
    strt=0
    endid =0
    for i in range(0, sze):
        endid=lenvl-sze+i+1
        arr=lstvl[strt:endid]
        print(i, strt, endid, arr)
        res=get_max_start(arr)
        strt=res[1]+1+strt
        lsteq.append(res[0])
    vl=lst_to_int(lsteq)
    return vl

def get_max_subset(lnevl:str):
    vl=0
    lst=list(elm)
    print('len: ',len(lst), vl,lnevl)
    vl=get_max_block(lst, 12)
    return vl

fle=open('in.txt','r')
lnes=fle.readlines()
ansvl=0
vls=[]
for lne in lnes:
    elm=lne.strip()
    vl = get_max_subset(elm)
    print(elm, vl)
    vls.append(vl)
    ansvl+=vl
print('ans:=',ansvl, vls)
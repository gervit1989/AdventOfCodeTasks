
fle=open('in.txt','r')
lnes=fle.readlines()
ansvl=0
vls=[]
for lne in lnes:
    vl=0
    elm=lne.strip()
    lst=list(elm)
    print('len: ',len(lst), vl,elm)
    for i in range(len(lst)-1):
        elm1=lst[i]
        for j in range(i+1, len(lst)):
            elm2=lst[j]
            restr=elm1+elm2
            print(i, j, restr, vl)
            vl2=int(restr)
            if vl2>vl:
                vl=vl2
    print(elm, vl)
    #break
    vls.append(vl)
    ansvl+=vl
print('ans:=',ansvl, vls)
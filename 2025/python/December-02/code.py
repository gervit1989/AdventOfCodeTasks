fle=open('in.txt','r')
lne=fle.readline()
lnen=lne.split(",")
lsumval =0
lsumvals=[]
for elem in lnen:
    objs = elem.split('-')
    num1= int(objs[0])
    num2= int(objs[1])
    print('range: ', num1, num2)
    for elm in range(num1, num2+1):
        strelm =str(elm)
        lenelm=len(strelm)
        if lenelm%2 == 1:
            continue
        firstp=strelm[0:lenelm//2]
        secp=strelm[lenelm//2:]
        if firstp==secp:
            lsumvals.append(elm)
            print(elm)
lsumval=sum(lsumvals)
print(lsumval)
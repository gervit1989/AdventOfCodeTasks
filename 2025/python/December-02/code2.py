
def ExistsDuplicates(lne):
    lenelm = len(lne)

    for i in range(lenelm-1, 0,-1):
        if lenelm %i ==0:
            #print(i, lne)
            str1=lne[:i]
            strt=i
            endvl=strt+i
            qvl=0
            for j in range(0, lenelm//i-1):
                str2=lne[strt:endvl]
                #print(str2)
                if str1==str2:
                    qvl+=1
                strt+=i
                endvl+=i
            if lne=='111':
                #print(qvl)
                pass
            if qvl==lenelm//i-1:
                return True
    return False

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
        if ExistsDuplicates(strelm):
            lsumvals.append(elm)
            print(elm)
lsumval=sum(lsumvals)
print(lsumval)
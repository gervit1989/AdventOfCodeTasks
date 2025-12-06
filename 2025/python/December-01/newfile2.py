def chval(val,drct):
	qvl=val
	if drct=='R':
		qvl+=1
	else:
		qvl-=1
	if qvl==100:
		return 0
	elif qvl<0:
		return 99
	return qvl
def getr(st,dr,x):
	nmvl=st
	diff=0
	code=0
	rsvl=[]
	while diff <x:
		nmvl=chval(nmvl,dr)
		#print(nmvl)
		if nmvl==0:
			code+=1
		diff+=1
	rsvl.append(nmvl)
	rsvl.append(code)
	return rsvl

fle=open('in1.txt','r')
lne=fle.readline()
lnen=lne.split(" ")
print(len(lnen))
code=0
ind=0
value=50
for elem in lnen:
	if ind>5000:
		break
	ind+=1
	num=int(elem[1:])
	dir=elem[0]
	print(num,dir,value)
	rslts=getr(value,dir,num)
	value =rslts[0]
	code+=rslts[1]
	print(rslts)
	
print(code)
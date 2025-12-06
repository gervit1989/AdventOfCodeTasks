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
	if dir =='R':
		value+=num
	else:
		value-=num
	print(value)
	if value <0:
		value+=100*(abs(value//100)+0)
	if value >99:
		value-=100*(abs(value//100)+0)
	print(value)
	if value%100==0:
		code+=1
print(code)
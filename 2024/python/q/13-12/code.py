
def det(a,b,c,d):
    #print(a,b,c,d)
    return a*d-b*c

class Task:
    def __str__(self):
        return (f"{self.a1}*x+{self.a2}*y={self.c1}\n{self.b1}*x+{self.b2}*y={self.c2}")
    def __init__(self, s1, s2, s3, flag):
        #print(s1)
        cfs1 = s1.split(':')
        cfs1 = cfs1[1].split(',')
        #print(s2)
        cfs2 = s2.split(':')
        cfs2 = cfs2[1].split(',')
        #print(s3)
        cfs3 = s3.split(':')
        cfs3 = cfs3[1].split(',')
        self.a1 = int(cfs1[0].split('+')[1])
        self.b1 = int(cfs1[1].split('+')[1])

        self.a2 = int(cfs2[0].split('+')[1])
        self.b2 = int(cfs2[1].split('+')[1])

        self.c1 = int(cfs3[0].split('=')[1])
        self.c2 = int(cfs3[1].split('=')[1])
        if flag:
            self.flag = True
            self.c1 += 10000000000000
            self.c2 += 10000000000000
        else:
            self.flag = False
    def try_solve(self):
        det1 = det(self.a1, self.a2, self.b1, self.b2)
        det2 = det(self.c1, self.a2, self.c2, self.b2)
        det3 = det(self.a1, self.c1, self.b1, self.c2)
        print(det1, det2, det3)
        if det1 == 0 and det2 != 0 and det3 != 0:
            return 0
        count_a = det2/det1
        count_b = det3/det1
        print(count_a, count_b)
        if (not self.flag and (count_a >= 100 or count_b >=100) ) or count_b<0 or count_a<0:
            print("from bounds")
            return 0
        if not count_a.is_integer() or not count_b.is_integer():
            print("float")
            return 0
        return count_a*3+count_b*1
lines = []
with open("in.txt", 'r') as fin:
    lines = fin.readlines()
#print(*lines)

len1 = len(lines)
i=0
sum_val = 0
while True:
    print(i)
    tsk =Task(lines[i].strip(), lines[i+1].strip(),lines[i+2].strip(), True)
    print(tsk)
    ans = tsk.try_solve()
    print(ans)
    sum_val += ans
    #break
    i+=4
    if i>= len1:
        break
print("ans: ", sum_val)
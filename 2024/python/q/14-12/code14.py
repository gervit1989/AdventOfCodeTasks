from itertools import count

def print_state(rob_lst, lens):
    for row in range(lens[1]):
        strv = ''
        for col in range(lens[0]):
            countx = 0
            for robot in rob_lst:
                if robot.cur[0] == col and robot.cur[1] == row:
                    countx+=1
            strv += str(countx) if countx else '.'
        print(strv)

class Robot:
    def __init__(self, s1:str, s2:str):
        strs = s1.split('=')
        strs = strs[1].split(',')
        self.point=(int(strs[0]),int(strs[1]))
        self.cur = [self.point[0], self.point[1]]

        strs = s2.split('=')
        strs = strs[1].split(',')
        self.vel=(int(strs[0]),int(strs[1]))

    def step_by_one(self, bounds):
        #print("init: ", self.cur)
        pos_new = [self.cur[0] + self.vel[0], self.cur[1] + self.vel[1]]
        #print("propose: ", pos_new)
        pos_new[1] = (bounds[1] + pos_new[1]) % bounds[1]
        pos_new[0] = (bounds[0] + pos_new[0]) % bounds[0]
        self.cur = pos_new
    def step(self, time_steps, bounds):
        for i in range(time_steps):
            self.step_by_one(bounds)
            #print("i: ", i, " pos: ", self.cur)

    def quadrant(self, mediums):
        if self.cur[0] == med[0] or self.cur[1] == med[1]:
            return 0
        elif self.cur[0] < med[0]:
            return 1 if self.cur[1] < med[1] else 3
        else:
            return 2 if self.cur[1] < med[1] else 4
        return -1

    def __str__(self):
        return f"point={self.point}, vel = {self.vel}"


robots =[]
addr ='in.txt'
with open(addr, 'r') as fin:
    while True:
        line = fin.readline()
        if len(line) == 0 or line == "":
            break
        strs = line.strip().split(" ")
        robots.append(Robot(strs[0], strs[1]))
        #print(robots[-1])
time_var = 1#8270
lens =(101,103)
if addr == 'in1.txt':
    lens=(11,7)
print_state(robots, lens)
med = (lens[0]//2, lens[1]//2)
min_a = 0
pos = -1
answ1 = 0
for i in range(10000):
    mapx={}
    for robot in robots:
        robot.step_by_one(lens)
        ans = robot.quadrant(med)
        #print("init: ",robot.point, "cur: ", robot.cur, ", q: ", ans)
        if ans == 0:
            continue
        elif ans in mapx.keys():
            mapx[ans] +=1
        else:
            mapx[ans] =1
    answ = 1
    #print(mapx.items())
    for key, val in mapx.items():
        answ*=val
    if i == 0 or answ < min_a:
        min_a =answ
        pos = i+1
        print_state(robots, lens)
    if i == 99:
        answ1 = answ
    print("ans[",i,"]: ", answ)
print("part1: ", answ1)
print("part2: ", pos)

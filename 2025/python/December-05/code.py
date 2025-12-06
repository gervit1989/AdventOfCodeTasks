# чтение данных
def read_data(file_name: str):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data
class RangeInterval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def set_end(self, end):
        self.end = end

    def check_in(self, elm):
        if self.start <= elm <= self.end:
            return True
        return False
    def __gt__(self, other):
        return self.start > other.start
    def __str__(self):
        return str(self.start)+'-'+str(self.end)+'\n'
    def get_len(self):
        return (self.end - self.start+1)
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class RangeStorage:
    def __init__(self):
        self.ranges = []

    def append_range(self, start, end):
        need_sign=True
        rlen=len(self.ranges)
        for k in range(rlen):
            elm=self.ranges[k]
            if elm == RangeInterval(start, end):
                need_sign=False
                break
            if elm.check_in(start) and elm.check_in(end):
                need_sign=False
                break
            if elm.check_in(start) and not elm.check_in(end):
                need_sign=False
                self.ranges[k].set_end(end)
                break
        if need_sign:
            self.ranges.append(RangeInterval(start, end))

    def append_interval(self, intvl: RangeInterval):
        self.append_range(intvl.start, intvl.end)
    def get_len(self):
        vlen = 0
        for elm in self.ranges:
            vlen+=elm.get_len()
        return vlen

def part1(rule):
    in_arr = read_data('in.txt')
    ranges = []
    actuals=[]
    isranges=True
    for row in in_arr:
        if len(row) ==0:
            isranges =False
            continue
        if isranges:
            lst=row.split('-')
            ranges.append(RangeInterval(int(lst[0]), int(lst[1])))
        else:
            actuals.append(int(row))
    cntvl=0
    if rule == 1:
        for elm in actuals:
            for rng in ranges:
                if rng.check_in(elm):
                    cntvl+=1
                    break
    elif rule == 2:
        strg = RangeStorage()
        srt_ranges=ranges.copy()
        srt_ranges.sort()
        #print(*srt_ranges)

        for rng in srt_ranges:
            strg.append_interval(intvl=rng)

        cntvl=strg.get_len()
    print('ans: ', str(rule), str(cntvl))

part1(1)
part1(2)
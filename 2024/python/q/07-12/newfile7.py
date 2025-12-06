f = [l.strip() for l in open("in.txt","rt")]

def gen(n,ops): # all op sequences of length n
  if n==1: return ops
  r = []
  for oo in gen(n-1,ops):
    #print(oo)
    for o in ops: r.append(oo+o)
  return r

def calculate(n,o):
  s = n[0]
  for i in range(len(o)):
    if o[i]=="+": s += n[i+1]
    elif o[i]=="*": s *= n[i+1]
    else: s = int(str(s)+str(n[i+1]))
  return s

def solve(l,ops):
  r,t = l.split(": "); r=int(r) # result to get
  n = tuple(map(int,t.split())) # numbers
  for o in gen(len(n)-1,ops):
    # if r == 931690:
        #print(o,"\n")
    if calculate(n,o) == r:
      #print(l, o, "\n")
      out2 = open("rights1.txt", "a")
      out2.write(str(r)+": " + str(t.split(" ")) + "\n")
      out2.close()
      return r
  out1 = open("errs1.txt", "a")
  out1.write(str(r)+": " + str(t.split(" ")) + "\n")
  out1.close()
  return 0

gen(5, "*+")
#print(*gen(5, "*+"), sep="\n")
out_err = open("errs1.txt", "w")
out_err.write("data\n")
out_err.close()
out_r = open("rights1.txt", "w")
out_r.write("data\n")
out_r.close()
# solve(f[0],"+*")
#print(sum(solve(l,"+*") for l in f))
print(sum(solve(l,"+*&") for l in f))
InputList = []
with open("input.txt", "r") as data:
    for t in data:
        InputList.append(t.strip())
ValidChars = set()
for t in range(10):
    ValidChars.add(str(t))
ValidChars.add(",")

def Mulberry(String):
    CharSet = set(String)
    Check = CharSet - ValidChars
    if len(Check) > 0:
        return 0
    Terms = String.split(",")
    if len(Terms) != 2:
        return 0
    A, B = Terms
    if len(A) > 3 or len(B) > 3:
        return 0
    print(A,B)
    return int(A)*int(B)

Part1Answer = 0
Part2Answer = 0
MulsEnabled = True
for Line in InputList:
    for u in range(len(Line)):
        if Line.startswith("mul(", u):
            NewString = ""
            for t in range(8):
                NewLetter = Line[u+t+4]
                if NewLetter == ")":
                    NewAddition = Mulberry(NewString)
                    Part1Answer += NewAddition
                    if MulsEnabled:
                        Part2Answer += NewAddition
                    break
                else:
                    NewString += NewLetter
        elif Line.startswith("do()", u):
            MulsEnabled = True
        elif Line.startswith("don't()", u):
            MulsEnabled = False

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
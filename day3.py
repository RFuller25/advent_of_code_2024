import re
total = 0
with open(input(), 'r') as f: 
    for match in re.findall(r"mul\(\d+,\d+\)", f.read()):
        x,y = match.replace("mul(", "").replace(")", "").split(",")
        total += int(x) * int(y)

print(total)
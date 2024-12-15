import re
total = 0
with open(input(), 'r') as f: 
    f = f.read()
    better_f = re.sub(r"don't\(\).*?do\(\)", '', f, 0 , re.DOTALL)
    for match in re.findall(r"mul\(\d+,\d+\)", f):
        x,y = match.replace("mul(", "").replace(")", "").split(",")
        total += int(x) * int(y)

print(total)
l1 = []
l2 = []
[((inp:=input().split()), l1.append(int(inp[0])), l2.append(int(inp[1]))) for i in range(1000)]
print(sum([(l1[i] * l2.count(l1[i])) for i in range(1000)]))
l1 = []
l2 = []
[((inp:=input().split()), l1.append(int(inp[0])), l2.append(int(inp[1]))) for i in range(1000)]
l1.sort(), l2.sort()
print(sum([abs(l1[i] - l2[i]) for i in range(1000)]))
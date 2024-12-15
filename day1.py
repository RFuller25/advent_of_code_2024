l1 = []
l2 = []

for i in range(1000):
    x, y = input().split()
    l1.append(int(x))
    l2.append(int(y))

l1.sort()
l2.sort()

distance = 0
for i in range(1000):
    distance += abs(l1[i] - l2[i])

print(distance)
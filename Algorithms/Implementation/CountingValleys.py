n = int(input())
hike = input().strip()
level = valley = 0
for i in range(len(hike)):
    if hike[i] == 'D':
        level = level - 1
    if hike[i] == 'U':
        level = level + 1
        if level == 0:
            valley = valley + 1
print (valley)
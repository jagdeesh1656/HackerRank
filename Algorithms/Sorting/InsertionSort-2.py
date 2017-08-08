n = int(input())
arr = [int(temp) for temp in input().strip().split(' ')]
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while key < arr[j] and j >= 0:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j + 1] = key
    print (' '.join(map(str, arr)))
           
    
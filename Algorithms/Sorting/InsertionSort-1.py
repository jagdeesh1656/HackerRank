# def insertionSort(arr):    
#     if len(arr) == 2:
#         if arr[0] > arr[1]:
#             temp = arr[0]
#             arr[0] = arr[1]
#             arr[1] = temp
#     if len(arr) > 2:
#         temp = arr[len(arr) - 1]
#         for i in range(len(arr) - 2, -1, -1):
#             if (temp < arr[i]):
#                 arr[i + 1] = arr[i]
#             else:
#                 arr[i + 1] = temp
#     print (arr)

# m = 5
# ar = [2, 4, 6, 8, 3]
# insertionSort(ar)
def insertionSort(arr):    
    if len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
    if len(arr) > 2:
        temp = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            if (temp < arr[i]):
                arr[i + 1] = arr[i]
            else:
                arr[i + 1] = temp
    print (arr)

m = 5
arr = [2, 4, 6, 8, 3]
insertionSort(arr)
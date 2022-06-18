ranking_list = [56,23,12,62,98,45,1,4,36,78,43]
ranking_list2 = [10,9,8,7,6,5,4,3,2,1]
import math

def mergeSort(arr):
    if (len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left,right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left),mergeSort((right)))

def merge(left, right):
    result = []
    while left and right:
        if left [0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result




def middle_list(arr):
    middle = math.floor(len(arr)/2)
    print(middle)
    left,right = arr[:middle], arr[middle:]
    return left,right

print(mergeSort(ranking_list2))
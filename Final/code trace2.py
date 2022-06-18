lst = [1,4,2,1,3]
def rank_sort(lst):
    n = len(lst)
    for i in range(1,n):
        temp = lst[i]
        j = i-1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst
ans = rank_sort(lst)
print(ans)
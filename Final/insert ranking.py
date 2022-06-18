ranking_list = [56,23,12,62,98,45,1,4,36,78,43]

def insertionSort(ranking_list):
    for i in range(len(ranking_list)):
        index = i-1
        cur = ranking_list[i]

        while index >= 0 and ranking_list[index] > cur:
            ranking_list[index+1] = ranking_list[index]
            index -=1
        ranking_list[index+1] = cur

    return ranking_list

ans = insertionSort(ranking_list)
print(ans)
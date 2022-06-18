"""
Leetcode Medium
"""

all_sub_lists = ([1,2,3,4])


def subset(s_list,current_list, left_list):
    if len(left_list) == 0:
        print(current_list)
    for ch in s_list:
        if ch in left_list:
            # choose
            ele = current_list.pop()
            # explorer
            subset(current_list)


subset(all_sub_lists,[], all_sub_lists)
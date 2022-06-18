"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    subset = []
    list_sub_lists_helper(lst,subset)


def list_sub_lists_helper(lst,subset):
    if len(lst)== 0:
        print(subset)

    else:
        # Choose
        ele




if __name__ == '__main__':
    main()

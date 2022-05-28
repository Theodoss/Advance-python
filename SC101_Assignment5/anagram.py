"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    # read_dictionary()
    start = time.time()
    find_anagrams('stop')
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    # lst = []
    dct = {}
    with open(FILE, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            # lst.append(line)
            first_alpha = line[0]
            str_long = len(line)
            # 編寫帶兩個Key(字頭&長度)的數據庫結構
            if first_alpha not in dct:
                dct[first_alpha]= {str_long: line.split()}
            else:
                if str_long not in dct[first_alpha]:
                    dct[first_alpha][str_long] = line.split()
                else:
                    dct[first_alpha][str_long].append(line)



def find_anagrams(s):
    """
    :param s:
    :return:
    """
    str_len = len(s)
    ans_lst = []
    find_anagrams_helper(s,[],ans_lst)
    print(ans_lst)

    #創造所有可能組合'


def find_anagrams_helper(s, current_lst, ans_lst):
    if len(current_lst) == len(s):
        ans_lst.append("".join(current_lst))
    else:
        for ch in s:
            if ch in current_lst:
                pass
            else:
                # choose
                current_lst.append(ch)
                # explorer
                find_anagrams_helper(s, current_lst, ans_lst)
                # un-choose
                current_lst.pop()
            # if s ==

def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()

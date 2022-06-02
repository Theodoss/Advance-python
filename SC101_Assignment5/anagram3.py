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

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO:
    """
    verb_dict = read_dictionary()
    print(f'Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        text = input('Find anagrams for :')
        text = text.lower()
        if text == '-1':
            break
        else:
            start = time.time()
            find_anagrams(text, verb_dict)

            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


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
                dct[first_alpha] = {str_long: line.split()}
            else:
                if str_long not in dct[first_alpha]:
                    dct[first_alpha][str_long] = line.split()
                else:
                    dct[first_alpha][str_long].append(line)
    return dct


def find_anagrams(s, verb_dict):
    """
    :param s: input str
    :param verb_dict: file to look
    :return: None
    """
    ans_lst = []
    print(f'Start searching......')
    find_anagrams_helper(s, [], ans_lst, list(s), verb_dict)
    print(f'Find {len(ans_lst)} anagram : {ans_lst}')


def find_anagrams_helper(s, current_lst, ans_lst, contral_list, verb_dict):
    # 創造所有單字所有可能組合
    if len(current_lst) == len(s):
        ans_str = "".join(current_lst)
        # 避免nn&nn error
        if ans_str not in ans_lst:
            ans_lst.append(ans_str)
            print(f'Found:  {ans_str}')
    else:
        for ch in s:
            if ch not in contral_list:
                pass
            elif has_prefix("".join(current_lst) + ch, len(s), verb_dict) is True:
                # choose
                current_lst.append(ch)
                contral_list.remove(ch)  # 移除控制list
                # explorer
                find_anagrams_helper(s, current_lst, ans_lst, contral_list, verb_dict)
                # un-choose
                current_lst.pop()
                contral_list.append(ch)  # 移除控制list


def has_prefix(sub_s, str_len, dic):
    #　找尋當前list是否包含該開頭
    if sub_s != None and len(sub_s) >= 2:
        for i in range(len(dic[sub_s[0]][str_len])):
            if dic[sub_s[0]][str_len][i].startswith(sub_s) is True:
                return True
    else:
        return True



if __name__ == '__main__':
    main()

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
    start = time.time()
    verb_dict = read_dictionary()
    end = time.time()
    print(f'The speed of read_dictionary: {end - start} seconds.')
    print(f'Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        text = input('Find anagrams for :')
        text = text.lower()
        if text == '-1':
            break
        else:
            start = time.time()
            find_anagrams(text, verb_dict)
            ####################
            #                  #
            #       TODO:      #
            #                  #
            ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    # lst = []
    dct = {}
    with open(FILE, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            str_long = len(line)
            # 編寫帶兩個Key(字頭&長度)的數據庫結構
            if str_long not in dct:
                dct[str_long] = {}
                temp_dict = dct[str_long]
            else:
                temp_dict = dct[str_long]
                for i in range(str_long):
                    ch = line[i]
                    if i == str_long-1:
                        temp_dict[ch] = line
                    else:
                        if ch not in temp_dict:
                            temp_dict[ch] = {}
                            temp_dict = temp_dict[ch]
                        else:
                            temp_dict = temp_dict[ch]
    return dct


def find_anagrams(s, verb_dict):
    """
    :param s:
    :return:
    """
    ans_lst = []
    print(f'Start searching......')
    find_anagrams_helper(s, [], ans_lst, list(s), verb_dict)
    print(f'Find {len(ans_lst)} words of anagram')


def find_anagrams_helper(s, current_lst, ans_lst, contral_list, verb_dict):
    # 創造所有單字所有可能組合
    if len(current_lst) == len(s):
        ans_str = "".join(current_lst)
        # 避免nn&nn error
        if ans_str not in ans_lst:
            ans_lst.append(ans_str)
            print(ans_str)
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


def looking_dict(list, verb_dict):
    """
    :param s:
    :return:
    """
    for verb in list:
        if verb in verb_dict[len(verb)][verb[0]]:
            print(verb)


def has_prefix(sub_s, str_len, dic):
    if sub_s != None and len(sub_s) >= 2:
        temp_dict = dic[str_len]
        for i in range(len(sub_s)):
            # for sub_s[i] in temp_dict:
            word = sub_s[i]
            if i == len(sub_s) - 1 and sub_s[i] in temp_dict:
                return True
            elif sub_s[i] in temp_dict:
                temp_dict = temp_dict[sub_s[i]]
            else:
                return False
    else:
        return True



if __name__ == '__main__':
    main()

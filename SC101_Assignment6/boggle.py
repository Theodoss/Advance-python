"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time
import re

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():

    input_list = []
    i = 0
    # 利用while 當輸入錯誤可以重新輸入
    while len(input_list) < 4:
        temp_str = input(f'{i + 1} row of letters: ')
        temp_str = temp_str.lower()
        # 利用正則式限制輸入類型
        if re.match(r'\D\s\D\s\D\s\D', temp_str, re.I):
            second_list = []
            for ch in temp_str:
                if ch != " ":
                    second_list.append([ch])
            input_list.append(second_list)
            i += 1
        else:
            input_list = []
            i = 0
            print(f"Input is not legal!")


    # 測試用文字檔
    # input_list = [[['f'], ['y'], ['c'], ['l']], [['i'], ['o'], ['m'], ['g']], [['o'], ['r'], ['i'], ['l']],
    #                [['h'], ['j'], ['h'], ['u']]]

    # 建立字典
    dct = read_dictionary()

    start = time.time()
    # Find all possible words
    ans_list = []
    # 一般For迴圈遍歷開台第一個位置
    for i in range(4):
        for j in range(4):
            # 利用遞歸遍歷周圍路徑
            boggle_helper(input_list,[input_list[i][j][0]],i,j,[[i,j]],dct,ans_list)
    print(f'Found {len(ans_list)} words')
    end = time.time()

    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')

def boggle_helper(list,word,i,j,his_pos,dct,ans_list):
    for k in -1,0,1:
        for y in -1,0,1:
            if 0 <= i+k <= 3 and 0 <= j+y <= 3 and [i+k,j+y] not in his_pos:
                word.append(list[i+k][j+y][0])
                # 編寫歷史路徑
                his_pos.append([i+k,j+y])

                # 順路遇字加字, 如不在字典內end case! 解決room 跟 roomy問題！
                if has_prefix("".join(word), dct) is True:
                    if len(word) > 3:
                        join_word = "".join(word)[0:len(word)]
                        # 先看ans_list 比較快一點
                        if join_word not in ans_list:
                            if join_word in dct[word[0]][word[1]]:
                                # 加過的單字從字典刪除, 增加一點速度
                                dct[word[0]][word[1]].remove(join_word)
                                print(f'Found {join_word}')
                                ans_list.append(join_word)
                    # explorer
                    boggle_helper(list, word, i + k, j + y, his_pos, dct, ans_list)
                    
                #unchoose
                word.pop()
                his_pos.pop()
    return ans_list



def read_dictionary():

    """
	TODO: Build 二叉樹搜尋法
	"""

    dct = {}
    with open(FILE, 'r') as f:
        for line in f.readlines():
            if 4 <= len(line) < 7:
                # print(line)
                line = line.strip()
                # 使用line.split 轉成[]
                word_list = line.split()
                if line[0] not in dct:
                    dct[line[0]] = {line[1]: word_list}
                else:
                    if line[1] not in dct[line[0]]:
                        dct[line[0]][line[1]] = word_list
                    else:
                        dct[line[0]][line[1]].append(line)
    return dct


def has_prefix(sub_s,dct):

    if len(sub_s) == 1:
        if sub_s in dct:
            return True
    else:
        if len(sub_s) == 2:
            if sub_s[0] in dct and sub_s[1] in dct[sub_s[0]]:
                return True
        else:
            for dict_word in dct[sub_s[0]][sub_s[1]]:
                if dict_word.startswith(sub_s) is True:
                    return True


if __name__ == '__main__':
    main()

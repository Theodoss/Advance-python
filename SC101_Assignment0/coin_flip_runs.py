"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	str_number = ""  # 紀錄結果初始化
	print("Let's flip a coin!")
	num_run = input("Number of runs:")  # 次數輸入
	num_run = int(num_run)

	while (True):
		unequal_num = 0  # 計算字符個數
		number = r.randint(0, 1)  # 隨機生成0，1正反面
		if number == 1:  # H代表1，T代表0
			number = "H"
		else:
			number = "T"
		str_number = str_number + str(number)  # 字符累積結果
		# str_number="HHTHHTHHHTTHTT"
		length_str_number = len(str_number)
		if length_str_number < 2:  # 至少生成兩字符
			continue
		for i in range(0, length_str_number - 1):  # 循環訪問生成

			if str_number[i + 1] == str_number[i]:  # 當前字符和下一個相同
				if num_run == 1:  # 當輸入==1時
					print(str_number)
					return str_number
			if str_number[i] != str_number[i + 1] and (i >= 1) and (
					str_number[i] == str_number[i - 1]):  # 找連續字符的邊界，前一個下相同N+1個不同
				unequal_num = unequal_num + 1  # 累計符合的字符串

		if num_run == unequal_num:  # 結果呈現
			print(str_number[:length_str_number - 1])
			break
	return str_number

	pass


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

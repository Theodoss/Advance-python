# import random
#
# a = random.randint(1, 100)
# c = None
# i = 0
# d1 = 1
# d2 = 100
# while True:
#     i += 1
#     b = random.randint(d1, d2)
#     if i == 7:
#         print('超出次数')
#         c = str(input('是否重玩？'))
#         if c == 'y':
#             i = 0
#             a = random.randint(1, 100)
#             d1 = 1
#             d2 = 100
#         elif c == 'n':
#             pass
#     else:
#         if b == a:
#             print(b, '正确', i)
#             c = str(input('是否重玩？'))
#             i = 0
#         elif b > a:
#             print(b, '大了', i)
#             d2 = b - 1
#         elif b < a:
#             print(b, '小了', i)
#             d1 = b - 1
# print('谢谢')

ans_lst = []
current_lst = []

print(ans_lst)


# def find_anagrams_helper(s, current_lst, ans_lst):
#     # 創造所有單字所有可能組合
#     if len(current_lst) == len(s):
#         ans_str = "".join(current_lst)
#         # 避免nn&nn error
#         if ans_str not in ans_lst:
#             ans_lst.append(ans_str)
#     else:
#         for ch in s:
#             if ch not in s:  # 反向決定字母數量
#                 pass
#             else:
#                 # choose
#                 current_lst.append(ch)
#                 s = s.replace("", ch)  # 移除控制list
#                 # explorer
#                 find_anagrams_helper(s, current_lst, ans_lst)
#                 # un-choose
#                 current_lst.pop()
#                 s = s + ch  # 移除控制list
#
#
# find_anagrams_helper("foood", current_lst, ans_lst)

list = ["fod","food","foood","fooood","foooood" ]
list.remove("fod")
print(list)
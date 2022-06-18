def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	# 非常重要, 如果有return數值 壹定要Return回去！
	return helper(lst,target,len(lst)//2)

def helper(lst,target,mid_i):
	if len(lst) == 0:
		return False
	if lst[mid_i] == target:
		return True

	else:
		if lst[mid_i] > target:
			# 不包含mid_i
			new_lst = lst[: mid_i]
		else:
			# 包含 mid_i
			new_lst = lst[mid_i+1:]
		# 非常重要, 如果有return數值 壹定要Return回去！
		return helper(new_lst, target, len(new_lst)//2)


if __name__ == '__main__':
	main()

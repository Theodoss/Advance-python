"""
File: basic_permutations.py
Name:
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(3)


def binary_permutations(length):
	binary_permutations_helper(length,'')

def binary_permutations_helper(n, current_s):
	if len(current_s) == n:
		print(current_s)
	else:
		binary_permutations_helper(n, current_s.append('1'))
		current_s.pop()
		binary_permutations_helper(n, current_s.append('0'))
		current_s.pop()



if __name__ == '__main__':
	main()
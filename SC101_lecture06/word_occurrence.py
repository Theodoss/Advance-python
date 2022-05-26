"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_d ={}
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			# print(tokens)
			for token in tokens:
				# print(token)
				token = string_munipulation(token)
				#First time?
				if token not in word_d:
					word_d[token] =1
				else:
					# Not first time
					word_d[token] += 1
		# print_out_d(word_d)

def string_munipulation(s):
	ans = ''
	print(s)
	for ch in s :
		ch = ch.lower()
		# print(ch)
		if ch.isalpha() or ch.isdigit():
			ans += ch
	return ans

def print_out_d(d):
	for word, occurrence in sorted(d.items(), key=lambda t:t[1]):
		print(word, '->', occurrence)



# def print_out_d(d):
# 	"""
# 	: param d: (dict) key of type str is a word
# 					value of type int is the word occurrence
# 	---------------------------------------------------------------
# 	This function prints out all the info in d
# 	"""
# 	pass


if __name__ == '__main__':
	main()

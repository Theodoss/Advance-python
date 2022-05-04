"""
File: coin_flip_runs.py
Name: stanCode example answer
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
	This program will flip the coin until it reaches the input number of runs.
	"""
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	runs = 0
	is_in_a_row = False
	flips = r.choice('HT')		# Record all flip histories

	while num_run != runs:
		new_flip = r.choice('HT')
		if flips[-1] == new_flip:		# See if last two flips are the same
			if not is_in_a_row:
				runs += 1
				is_in_a_row = True
		else:
			is_in_a_row = False

		flips += new_flip

	print(flips)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
	param n:
	return:
	"""

    n = abs(n)
    n_count = n
    digit = 1
    ans = 0
    digit = fine_largest_digit_helper(n, digit)
    ans = fine_largest_digit_helper2(n, n_count, digit, ans)
    return ans


def fine_largest_digit_helper(n, digit):
    if n < 10:
        return digit
    else:
        n = n / 10
        digit += 1
        return fine_largest_digit_helper(n, digit)


def fine_largest_digit_helper2(n, n_count, digit, ans):
    if digit == 0:
        return ans
    else:
        digit -= 1
        if ans < n / (10 ** digit):
            ans = int(n / (10 ** digit))
        n = n - ans * (10 ** digit)
        return fine_largest_digit_helper2(n, n_count, digit, ans)


if __name__ == '__main__':
    main()

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
    n = abs(n)
    ans = 0
    ans = fine_largest_digit_helper(n, ans)
    return ans


def fine_largest_digit_helper(n, ans):
    if n < 10:
        if ans < n:
            ans = n
        return int(ans)
    else:
        # 比對浮點數第一位大小
        if ans < n - (n // 10) * 10:
            ans = n - (n // 10) * 10
        # 扣掉個位數並除以10
        n = (n - (n - (n // 10) * 10)) / 10
        return fine_largest_digit_helper(n, ans)


if __name__ == '__main__':
    main()

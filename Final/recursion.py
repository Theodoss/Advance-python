def digit_sum_helper(num,ans,a):
    if num < 10:
        ans += num
        if a is True:
            ans = ans * (-1)
        return ans
    else:
        temp = num % 10
        ans += temp
        num = num // 10
        return digit_sum_helper(num,ans,a)

def digit_sum(num):
    ans = 0
    if num < 0:
        a = True
    return digit_sum_helper(abs(num),ans,a)



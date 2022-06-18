def digit_sum_helper(num):
    if num < 10:
        return True
    else:
        temp1 = num % 10
        num = num // 10
        temp2 = num % 10
        if temp1 < temp2:
            return False
        return digit_sum_helper(num)

def digit_sum(num):
    return digit_sum_helper(abs(num))

print(digit_sum(-3331))
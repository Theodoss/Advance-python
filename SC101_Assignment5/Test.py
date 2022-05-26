import random

a = random.randint(1, 100)
c = None
i = 0
d1 = 1
d2 = 100
while True:
    i += 1
    b = random.randint(d1, d2)
    if i == 7:
        print('超出次数')
        c = str(input('是否重玩？'))
        if c == 'y':
            i = 0
            a = random.randint(1, 100)
            d1 = 1
            d2 = 100
        elif c == 'n':
            pass
    else:
        if b == a:
            print(b, '正确', i)
            c = str(input('是否重玩？'))
            i = 0
        elif b > a:
            print(b, '大了', i)
            d2 = b - 1
        elif b < a:
            print(b, '小了', i)
            d1 = b - 1
print('谢谢')
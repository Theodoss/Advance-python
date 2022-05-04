import pypal


def bank():
    theo_a = pypal.Pypal('Theo', money=2000, withdraw_limit=800)
    theo_a.get_money()
    theo_a.set_username('Theodos')
    theo_a.withdraw(1000)
    theo_a.withdraw(700)
    theo_a.withdraw(700)

    # theo_a.__m = 10000000 # strict private猜到變數,也不會有用, 但也不會出error
    theo_a._m = 10000000  # soft private 看不到變數, 但猜到變數,也可以改
    theo_a._w_l = 10000


if __name__ == '__main__':
    bank()

WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self._w_l = withdraw_limit

    # Getter
    def get_money(self):
        return self.__m

    #Setter
    def set_username(self, new_name):
        self._n = new_name

    def withdraw(self, amount):
        if amount > self._w_l:
            print('Exceed Limit')
        elif amount > self.__m:
            print('Illegal')
        else:
            self.__m -= amount
            print(f"{self._n}: {self.__m}")


def bank():
    theo_a = Pypal('Theo', money=1000, withdraw_limit=800)
    theo_a.withdraw(1000)
    theo_a.withdraw(700)
    theo_a.withdraw(700)


if __name__ == '__main__':
    bank()

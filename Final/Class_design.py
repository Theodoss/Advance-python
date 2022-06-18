class Theater:
    def __init__(self,n):
        self.seats_list = []
        for i in range(5):
            self.seats_list.append(1)

    def reserve(self):
        if 1 in self.seats_list:
            for i in range(len(self.seats_list)):
                if self.seats_list[i] == 1:
                    self.seats_list[i] = 0
                    print(i+1)
                    break

        else:
            print("There is no seats available")

    def unreserve(self,seat_numbers):
        if self.seats_list[seat_numbers-1] == 0:
            self.seats_list[seat_numbers-1] = 1
        else:
            print("There is no seats available")

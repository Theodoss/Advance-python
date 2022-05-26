from campy.graphics.gobjects import GOval,GRect


class Robot:
    # Constructor
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        # color 應該存在一個記憶體地址中?
        self.c = color
        self.color #但無法直接調用
    def self_intro(self):
        print(f'h={self.h}/w={self.w}')

    def bmi(self):
        # weight / (h_in_meter**2)
        h_in_meter = self.h/100
        print('BMI:', self.w/(h_in_meter**2))

    @staticmethod
    def say_hi():
        print("Hi!")


    # Method
    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

class Robot2(Robot):
    def __init__(self, hegiht2, weight2, color2='green', count2=3):
        super().__init__(hegiht2, weight2, color=color2)
        self.count = count2

    def start_count(self):
        for i in range(self.count):
            print(i+1)

class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3 ,color3='green', count3=3):
        super().__init__(height3, weight3, color2=color3, count2=count3)
        self.r_c =rect_color3

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect

if __name__ == '__main__':
    print('[robot.py]__:',__name__)

if __name__ == 'robot':
    print('Thanks for using robot.py')
    print('Please use Robot3 only. Beacuse it is the updated one')

print("1234")
from robot import Robot,Robot2,Robot3
from campy.graphics.gwindow import GWindow

window = GWindow()
def main():
    r1 = Robot(183, 70, 'blue' )
    r2 = Robot(160,50)
    # print(r1.w)
    # print(r1.h)
    #
    # ball1 = r1.give_me_a_ball(200)
    # ball2 = r2.give_me_a_ball(150)
    #
    # window.add(ball1)
    # window.add(ball2)

    # r1.self_intro()
    # r2.self_intro()
    # r1.bmi()
    # r2.bmi()
    #
    # r1.say_hi()
    # Robot.say_hi()

    r3= Robot3(100,10,'red','green',count3=10)
    r3.bmi()
    r3.give_me_a_rect(150)
    r3.give_me_a_ball(200)
    r3.self_intro()

    window.add(r3.give_me_a_rect(150))

if __name__ == '__main__':
    main()

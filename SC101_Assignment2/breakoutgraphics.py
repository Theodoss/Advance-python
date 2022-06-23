"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
import cmath

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # 7Initial vertical speed for the ball
MAX_X_SPEED = 5  # 5Maximum initial horizontal speed for the ball


# Global variable


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                             y=window_height - paddle_offset)
        self._paddle.filled = True
        self.window.add(self._paddle)

        # Center a filled ball in the graphical window
        # self.ball = GOval(ball_radius, ball_radius, x=self.paddle.x + (paddle_width - ball_radius) / 2,
        #                   y=self.paddle.y - ball_radius)
        self.ball = GOval(ball_radius, ball_radius, x=window_width / 2, y=window_height / 2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.is_moving = False
        self.dead_switch = False
        onmouseclicked(self.click)

        # Initialize our paddle move with mouse
        onmousemoved(self.paddle_move)

        # Draw bricks
        # #為什麼要額為賦直?
        self._brick_width = brick_width
        self._brick_height = brick_height
        self._brick_offset = brick_offset
        self._brick_spacing = brick_spacing
        self._brick_row = brick_rows
        self._brick_cols = brick_cols
        self.draw_brick()

        # Count brick life
        self._brick_num = brick_rows * brick_cols

        # initial some global variable
        self._bounce_switch = None
        self.brick_num = None
        self.dead_switch = False

    def click(self, event):
        if self.is_moving is False and event.x > 0:
            self.is_moving = True

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    def x_bounce(self):
        self.__dx *= -1

    def y_bounce(self):
        self.__dy *= -1

    def draw_brick(self):
        for i in range(self._brick_row):
            for j in range(self._brick_cols):
                brick_i_j = GRect(self._brick_width, self._brick_height,
                                  x=(self._brick_width + self._brick_spacing) * i,
                                  y=self._brick_offset + (self._brick_height + self._brick_spacing) * j)
                brick_i_j.filled = True
                if j <= 1:
                    brick_i_j.fill_color = "blue"
                if 1 < j <= 3:
                    brick_i_j.fill_color = "green"
                if 3 < j <= 5:
                    brick_i_j.fill_color = "gold"
                if 5 < j <= 7:
                    brick_i_j.fill_color = "orange"
                if 7 < j <= 9:
                    brick_i_j.fill_color = "red"
                self.window.add(brick_i_j)

    # Paddle
    def paddle_move(self, event):
        if event.x < self._paddle.width / 2:
            self._paddle.x = 0
        elif event.x > self.window.width - self._paddle.width / 2:
            self._paddle.x = self.window.width - self._paddle.width
        else:
            self._paddle.x = event.x - self._paddle.width / 2

    # 相位方式碰撞


    # 利用八點進行碰撞檢測
    def ball_bounce(self):
        # 建立八角等距碰撞檢測點
        ball_point1 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_point2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ball_point3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ball_point4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # 正上
        ball_point5 = self.window.get_object_at(self.ball.x + self.ball.width / 2, self.ball.y - self.ball.width * 0.4)
        # 正右
        ball_point6 = self.window.get_object_at(self.ball.x + self.ball.width + self.ball.width * 0.4, self.ball.y + self.ball.height / 2)
        # 正下
        ball_point7 = self.window.get_object_at(self.ball.x + self.ball.width / 2, self.ball.y + self.ball.height + self.ball.width * 0.4)
        # 正左
        ball_point8 = self.window.get_object_at(self.ball.x - self.ball.width * 0.4, self.ball.y + self.ball.height / 2)

        # 檢測是否可以碰撞
        if self._bounce_switch is True:
            # 檢測四邊是否碰撞
            if bool(ball_point1) is True or bool(ball_point2) is True or bool(ball_point3) is True \
                    or bool(ball_point4) is True or bool(ball_point5) is True or bool(ball_point6) is True\
                    or bool(ball_point7) is True or bool(ball_point8) is True:
                # 先檢測雙點碰撞跟速度檢測
                if bool(ball_point5) is True and self.__dy < 0: # 正上方
                    print(f'bounce_5')
                    self.y_bounce()
                    self._bounce_switch = False
                    bounce_object = ball_point5
                    # 檢測消除單位
                    if bounce_object is not self._paddle:
                        self.window.remove(bounce_object)
                        self._brick_num -= 1
                elif bool(ball_point6) is True and self.__dx > 0: # 正右邊
                    print(f'bounce_6')
                    self.x_bounce()
                    self._bounce_switch = False
                    bounce_object = ball_point6
                    if bounce_object is not self._paddle:
                        self.window.remove(bounce_object)
                        self._brick_num -= 1
                elif bool(ball_point7) is True and self.__dy > 0: # 正下邊
                    print(f'bounce_7')
                    self.y_bounce()
                    self._bounce_switch = False
                    bounce_object = ball_point7
                    if bounce_object is not self._paddle:
                        self.window.remove(bounce_object)
                        self._brick_num -= 1
                elif bool(ball_point8) is True and self.__dx < 0: # 正左邊
                    print(f'bounce_8')
                    self.x_bounce()
                    self._bounce_switch = False
                    bounce_object = ball_point8
                    if bounce_object is not self._paddle:
                        self.window.remove(bounce_object)
                        self._brick_num -= 1
                # # 檢測單點碰撞
                # elif bool(ball_point1) is True:
                #     if self.__dx > 0 or self.__dy > 0:
                #         self.x_bounce()
                #         self.y_bounce()
                #         self._bounce_switch = False
                #         bounce_object = self.window.get_object_at(ball_point1.x, ball_point1.y)
                #         if bounce_object is not self._paddle:
                #             self.window.remove(bounce_object)
                #             self._brick_num -= 1
                # elif bool(ball_point2) is True:
                #     if self.__dx < 0 or self.__dy > 0:
                #         self.x_bounce()
                #         self.y_bounce()
                #         self._bounce_switch = False
                #         bounce_object = self.window.get_object_at(ball_point2.x, ball_point2.y)
                #         if bounce_object is not self._paddle:
                #             self.window.remove(bounce_object)
                #             self._brick_num -= 1
                # elif bool(ball_point3) is True:
                #     if self.__dx > 0 or self.__dy < 0:
                #         self.x_bounce()
                #         self.y_bounce()
                #         self._bounce_switch = False
                #         bounce_object = self.window.get_object_at(ball_point3.x, ball_point3.y)
                #         if bounce_object is not self._paddle:
                #             self.window.remove(bounce_object)
                #             self._brick_num -= 1
                # elif bool(ball_point4) is True:
                #     if self.__dx < 0 or self.__dy < 0:
                #         self.x_bounce()
                #         self.y_bounce()
                #         self._bounce_switch = False
                #         bounce_object = self.window.get_object_at(ball_point4.x, ball_point4.y)
                #         if bounce_object is not self._paddle:
                #             self.window.remove(bounce_object)
                #             self._brick_num -= 1
        if bool(ball_point1) is False and bool(ball_point2) is False and bool(ball_point3) is False \
                and bool(ball_point4) is False:
            self._bounce_switch = True

    def ball_reset(self, life):
        print(life)
        if life > 0:
            self.ball.x, self.ball.y = (self.window.width / 2, self.window.height / 2)
            self.is_moving = False
        else:
            died_icon = GLabel("YOU DIED", 100, self.window.height / 2 + 80)
            died_icon.color = "red"
            died_icon.font = "SansSerif-60"
            self.ball.x, self.ball.y = (self.window.width / 2, self.window.height / 2)
            self.is_moving = False
            self.dead_switch = True
            self.window.add(died_icon)

    def you_win(self):
        if self.brick_num == 0:
            win_icon = GLabel("YOU WIN", 50, self.window.height / 2 + 80)
            win_icon.color = "blue"
            win_icon.font = "SansSerif-60"
            self.window.add(win_icon)

    def side_bounce(self):
        # 邊界反彈，底面不反彈
        if self.ball.x <= 0 and self.__dx < 0:
            self.x_bounce()
        elif self.ball.x + self.ball.width >= self.window.width and self.__dx > 0:
            self.x_bounce()
        elif self.ball.y <= 0 and self.__dy < 0:
            self.y_bounce()

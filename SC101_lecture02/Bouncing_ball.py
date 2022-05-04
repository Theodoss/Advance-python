"""
File: SC101_Assignment1
Name: Bouncing_ball
------------------------

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

# Constants 設定
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
X_START = 30
Y_START = 40

# Global variance
click_starter = None  # 開關起始設置

window = GWindow(800, 500, title='Bouncing_Ball')
oval = GOval(SIZE, SIZE)
window.add(oval, x=X_START, y=Y_START)


def main():
    """
    This file shows how to use campy
    mouse event to start a gravity-bouncing-reduce simulation
    :return:
    """
    onmouseclicked(Bouncing_ball)  # 啟動監聽器


def Bouncing_ball(mouse):
    global click_starter
    vy = 0  # 設定初始落下速度
    bounce_counter = 0  # 設定反彈次數
    if click_starter is None:  # 檢測前一個點擊狀態
        click_starter = mouse.x  # 點擊後開關關閉
        while bounce_counter < 3:  # 檢測視窗外彈跳情況
            oval.move(VX, vy)
            vy += GRAVITY  # 設定重力加速度at
            if oval.y + oval.height >= window.height and vy_past >= 0: # 判斷前一個速度直是否為正
                vy = -vy * REDUCE  # 反彈並設定反彈係數
                if oval.x >= window.width:
                    # 畫面外反彈計數器+1
                    bounce_counter += 1
                    print(f'畫面外彈跳次數: {bounce_counter}')
            vy_past = vy # 儲存前一個速度直
            pause(DELAY)

        print("Back to start point! APP end!")
        click_starter = None  # 開關復位
        oval.x, oval.y = (X_START, Y_START)  # 將球復位


if __name__ == '__main__':
    main()

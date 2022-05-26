"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    gp = BreakoutGraphics()
    life = NUM_LIVES
    # Add the animation loop here!
    while True:
        # 起始點擊開關
        if gp.is_moving is True and gp.dead_switch is False:
            gp.ball.move(gp.dx, gp.dy)
        # 反彈檢測
        gp.side_bounce()
        # 掉底扣一條命
        if gp.ball.y + gp.ball.height >= gp.window.height:
            gp.ball_reset(life)
            life -= 1
        # 反彈檢測
        gp.ball_bounce()
        # 勝利檢測
        gp.you_win()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()

    while True:
        # Update
        # vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics._ball.move(graphics.vx, vy)
        lives = NUM_LIVES
        # Chick
        if graphics.ball_in_zone() is True:
            graphics.reset_ball()
        if graphics._ball.x <= 0 or graphics._ball.x + graphics._ball.width > graphics._window.width:
            graphics.set_vx()
        if graphics._ball.y <= 0 or graphics._ball.y + graphics._ball.height > graphics._window.height:
            graphics.set_vy()
        if graphics.ball_in_zone():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                print("Game end")
                break

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

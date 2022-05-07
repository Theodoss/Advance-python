"""
File: ans_bouncing_ball.py
Name: stanCode example answer
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3          # Controls the horizontal speed of the ball
DELAY = 10      # Frame rate
GRAVITY = 1     # Simulates the value of gravity
SIZE = 20       # The diameter of the ball
REDUCE = 0.9    # Controls how high proportion
START_X = 30    # The start x-axis position
START_Y = 40    # The start y-axis position

window = GWindow(800, 500, title='ans_bouncing_ball.py')
is_moving = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to a value of REDUCE of itself.
    """
    global is_moving

    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.color = 'black'
    ball.filled = True
    window.add(ball)

    vy = 0      # Default value of vy
    count = 0   # Counts how many times the ball goed out of the window

    onmouseclicked(start)

    while True:
        if is_moving and count < 3:

            ball.move(VX, vy)
            vy += GRAVITY

            # Rebound when the ball hits the ground
            if ball.y + ball.height > window.height:
                if vy > 0:      
                    vy *= - REDUCE

            # Reset when the ball goes out of the window
            if ball.x > window.width:
                vy = 0
                ball.x = START_X
                ball.y = START_Y
                is_moving = False
                count += 1

        pause(DELAY)


def start(event):
    """
    Allows the ball to move.
    """
    global is_moving
    is_moving = True


if __name__ == "__main__":
    main()

"""
File: draw_line_sol2.py
Name: stanCode example answer
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants
SIZE = 20   # The diameter of the circle

# Global Variables
circle = GOval(SIZE, SIZE)
window = GWindow(800, 500, title='draw_line.py')

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_circle)


def draw_circle(event):
    """
    params(event): MouseEvent, stores the information of mouse positions.
    --------------
    This function controls what to do when the user clicks on the window.
    """
    circle.x = event.x - SIZE // 2
    circle.y = event.y - SIZE // 2
    window.add(circle)
    onmouseclicked(draw_line)


def draw_line(event):
    """
    params(event): MouseEvent, stores the information of mouse positions.
    --------------
    This function controls what to do when the user clicks on the window.
    """
    window.remove(circle)
    line = GLine(circle.x + SIZE // 2, circle.y + SIZE // 2, event.x, event.y)
    window.add(line)
    onmouseclicked(draw_circle)


if __name__ == "__main__":
    main()

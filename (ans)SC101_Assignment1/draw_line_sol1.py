"""
File: draw_line_sol1.py
Name: stanCode example answer
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants
SIZE = 20       # The diameter of the circle

# Global Variables
count = 0       # Counts how many times the user has clicked

circle = GOval(SIZE, SIZE)
window = GWindow(800, 500, title='draw_line.py')

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    """
    params(event): MouseEvent, stores the information of mouse positions.
    --------------
    This function controls what to do when the user clicks on the window.
    """
    global count
    count += 1

    if count % 2 == 1:
        circle.x = event.x - SIZE // 2
        circle.y = event.y - SIZE // 2
        window.add(circle)
    else:
        window.remove(circle)
        line = GLine(circle.x + SIZE // 2, circle.y + SIZE // 2, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()

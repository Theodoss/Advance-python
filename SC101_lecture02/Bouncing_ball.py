"""
File: SC101_Assignment1
Name: Bouncing_ball
------------------------
This file shows how to use campy
mouse event to start a gravity-bouncing simulation
"""


from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLine

# This constant controls the size of the pen stroke
SIZE = 10
window = GWindow(500, 500,title = 'Draw_line')

def main():
    onmouseclicked(Bouncing_ball)

def Bouncing_ball(mouse):







if __name__ == '__main__':
        main()

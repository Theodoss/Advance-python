"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 1
window = GWindow(500, 500,title = 'mouse_draw')

def main():
	onmousedragged(create_hole)


def create_hole(mouse):
	pen_stroke = GOval(SIZE, SIZE)
	pen_stroke.color = 'blue'
	pen_stroke.filled = True
	pen_stroke.fill_color = 'blue'
	window.add(pen_stroke, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
	main()

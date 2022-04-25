"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the GRect
SIZE = 50
#Global Variable

window=GWindow(500,500)
rect = GRect(SIZE, SIZE)



def main():
	onmousemoved(change_position)
	rect.filled = True

	window.add(rect)

def change_position(mouse):
	rect.x =mouse.x-SIZE/2
	rect.y =mouse.y-SIZE/2

	if rect.x >= window.width/2 and rect.y <= window.height / 2:
		rect.fill_color ='blue'
		rect.filled = 'blue'
	elif rect.y >= window.height / 2 and rect.x <= window.width/2:
		rect.fill_color ='black'
		rect.filled = 'black'
	elif rect.y <= window.height / 2 and rect.x <= window.width/2:
		rect.fill_color ='green'
		rect.filled = 'green'

	else:
		rect.fill_color = 'magenta'
		rect.filled = 'magenta'


if __name__ == '__main__':
	main()

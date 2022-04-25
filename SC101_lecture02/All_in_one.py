from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved
from campy.gui.events.mouse import onmousedragged
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GRect
SIZE = 50
#Global Variable
window=GWindow(500,500)
rect = GRect(SIZE, SIZE)



def main():
	onmousemoved(change_position)
	onmousedragged(create_hole)
	onmouseclicked(create_hole)
	rect.filled = True

	window.add(rect)

def change_position(mouse):
	rect.x =mouse.x-SIZE/2
	rect.y =mouse.y-SIZE/2

	if rect.x >= window.width/2 and rect.y <= window.height / 2:
		rect.fill_color ='blue'
		rect.filled = 'blue'
	else:
		rect.fill_color = 'magenta'
		rect.filled = 'magenta'

def create_hole(mouse):
	pen_stroke = GRect(SIZE, SIZE)

	if mouse.x >= window.width/2:
		pen_stroke.fill_color ='blue'
		pen_stroke.filled = 'blue'
	else:
		pen_stroke.fill_color = 'magenta'
		pen_stroke.filled = 'magenta'
	pen_stroke.filled = True
	window.add(pen_stroke, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
	main()
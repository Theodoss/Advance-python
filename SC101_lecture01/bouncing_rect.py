"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""
from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


# This controls the width and height of the rect
SIZE = 30
# This controls the pause time (in millisecond) for the animation
DELAY = 10


def main():
	window = GWindow(width= 500, height= 500, title = 'Animate1')
	Oval1 = GOval(SIZE,SIZE)
	Oval1.filled = True
	Oval1.color ="blue"
	Oval2 = GOval(SIZE, SIZE)
	Oval2.filled = True
	Oval2.color ="green"

	# Oval3 = GOval(SIZE, SIZE)
	window.add(Oval1, x=(window.width - SIZE)/2,  y= (window.height-SIZE)/2)
	window.add(Oval2, x=1, y= (window.height-SIZE)/2)
	# window.add(Oval3, x=1, y=1)
	Oval1_vx = 1
	Oval1_vy = 0
	Oval2_vx = 1
	Oval2_vy = 0
	while True:
		Oval1.move(Oval1_vx, Oval1_vy)
		Oval2.move(Oval2_vx, Oval2_vy)
		#球一行為
		if Oval1.x <= 0 or Oval1.x+Oval1.width >= window.width:
			Oval1_vx = -Oval1_vx
		if Oval1.y <= 0 or Oval1.y+Oval1.height >= window.height:
			Oval1_vy = -Oval1_vy
		# 球一碰撞檢測
		if  Oval2.x <= Oval1.x <= Oval2.x + Oval2.width or Oval2.x <= Oval1.x+Oval1.width <= Oval2.x + Oval2.width:
			if Oval2.y <= Oval1.y <= Oval2.y+ Oval2.height or Oval2.y <= Oval1.y+Oval1.height <= Oval2.y+Oval2.height :
				Oval1_vx = -Oval1_vx
		if Oval2.y <= Oval1.y <= Oval2.y + Oval2.height or Oval2.y <= Oval1.y+Oval1.height <= Oval2.y+Oval2.height:
			if Oval2.y <= Oval1.y >= Oval2.y + Oval2.width or Oval2.y <= Oval1.y + Oval1.height <= Oval2.y + Oval2.height:
				Oval1_vy = -Oval1_vy

		# 球二行為
		if Oval2.x <= 0 or Oval2.x+Oval2.width >= window.width:
			Oval2_vx = -Oval2_vx
		if Oval2.y <= 0 or Oval2.y+Oval2.height >= window.height:
			Oval2_vy = -Oval2_vy
		#球二碰撞檢測
		if  Oval1.x <= Oval2.x <= Oval1.x + Oval1.width or Oval1.x <= Oval2.x+Oval2.width <= Oval1.x + Oval1.width:
			if Oval1.y <= Oval2.y <= Oval1.y+ Oval1.height or Oval1.y <= Oval2.y+Oval2.height <= Oval1.y+Oval1.height :
				Oval2_vx = -Oval2_vx
		if Oval1.y <= Oval2.y <= Oval1.y + Oval1.height or Oval1.y <= Oval2.y+Oval2.height <= Oval1.y+Oval1.height:
			if Oval1.y <= Oval2.y >= Oval1.y + Oval1.width or Oval1.y <= Oval2.y + Oval2.height <= Oval1.y + Oval1.height:
				Oval2_vy = -Oval2_vy



		pause(10)
	pass

def buncing_dect():
	if Oval1.x <= Oval2.x <= Oval1.x + Oval1.width or Oval1.x <= Oval2.x + Oval2.width <= Oval1.x + Oval1.width:
		if Oval1.y <= Oval2.y <= Oval1.y + Oval1.height or Oval1.y <= Oval2.y + Oval2.height <= Oval1.y + Oval1.height:
			Oval2_vx = -Oval2_vx
	if Oval1.y <= Oval2.y <= Oval1.y + Oval1.height or Oval1.y <= Oval2.y + Oval2.height <= Oval1.y + Oval1.height:
		if Oval1.y <= Oval2.y >= Oval1.y + Oval1.width or Oval1.y <= Oval2.y + Oval2.height <= Oval1.y + Oval1.height:
			Oval2_vy = -Oval2_vy

if __name__ == '__main__':
	main()

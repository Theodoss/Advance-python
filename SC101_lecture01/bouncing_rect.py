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

def bouncing_dectect(obj1,obj2, obj1_vx, obj1_vy):
	if obj1.x <= obj2.x <= obj1.x + obj1.width or obj1.x <= obj2.x + obj2.width <= obj1.x + obj1.width:
		if obj1.y <= obj2.y <= obj1.y + obj1.height or obj1.y <= obj2.y + obj2.height <= obj1.y + obj1.height:
			obj1_vx = -obj1_vx
			return obj1_vx, obj1_vy
	if obj1.y <= obj2.y <= obj1.y + obj1.height or obj1.y <= obj2.y+obj2.height <= obj1.y+obj1.height:
		if obj1.y <= obj2.y >= obj1.y + obj1.width or obj1.y <= obj2.y + obj2.height <= obj1.y + obj1.height:
			obj1_vy = -obj1_vy
			return obj1_vx, obj1_vy
	else:
		return obj1_vx, obj1_vy

			

def bouncing_border(obj, obj_vx, obj_vy, window):
	if obj.x <= 0 or obj.x + obj.width >= window.width:
		obj_vx = -obj_vx
	if obj.y <= 0 or obj.y + obj.height >= window.height:
		obj_vy = -obj_vy
		return obj_vx, obj_vy
	else:
		return obj_vx, obj_vy

def main():
	window = GWindow(width= 500, height= 500, title = 'Animate1')

	Oval1 = GOval(SIZE,SIZE)
	Oval1.filled = True
	Oval1.fill_color ="blue"
	Oval1_vx = 1
	Oval1_vy = 1
	window.add(Oval1, x=100,  y= (window.height-SIZE)/2)

	Oval2 = GOval(SIZE, SIZE)
	Oval2.filled = True
	Oval2.fill_color ="blue"
	Oval2_vx = 0
	Oval2_vy = 1
	window.add(Oval2, x=200, y= (window.height-SIZE)/2)

	Oval3 = GOval(SIZE, SIZE)
	Oval3.filled = True
	Oval3.fill_color ="blue"
	Oval3_vx = 1
	Oval3_vy = 0
	window.add(Oval3, x=300, y= (window.height-SIZE)/2)

	Oval4 = GOval(SIZE, SIZE)
	Oval4.filled = True
	Oval4.fill_color ="blue"
	Oval4_vx = 1
	Oval4_vy = 0
	window.add(Oval4, x=400, y= (window.height-SIZE)/2)

	List = ["Oval1", "Oval2", "Oval3", "Oval4"]
	# window.add(Oval3, x=1, y=1)

	while True:
		Oval1.move(Oval1_vx, Oval1_vy)
		Oval2.move(Oval2_vx, Oval2_vy)
		Oval3.move(Oval3_vx, Oval3_vy)

		Oval1_vx, Oval1_vy = bouncing_border(Oval1, Oval1_vx, Oval1_vy, window)
		Oval2_vx, Oval2_vy = bouncing_border(Oval2, Oval2_vx, Oval2_vy, window)
		Oval3_vx, Oval3_vy = bouncing_border(Oval3, Oval3_vx, Oval3_vy, window)

		for i in range(len(List)):
			for j in range(len(List)):
				locals()[str(i) + '_vx'] = List[i]
				vx = locals()[str(i)+"_1234vx"]
				print(vx)
				locals()[str(i) + '_vy'] = i
				vy = locals()[str(i) + '_vy']
				print(vy)
				vx,vy= bouncing_dectect(i,j,vx,vy)



		# #球一行為
		# if Oval1.x <= 0 or Oval1.x+Oval1.width >= window.width:
		# 	Oval1_vx = -Oval1_vx
		# if Oval1.y <= 0 or Oval1.y+Oval1.height >= window.height:
		# 	Oval1_vy = -Oval1_vy
		# # 球一碰撞檢測
		# if  Oval2.x <= Oval1.x <= Oval2.x + Oval2.width or Oval2.x <= Oval1.x+Oval1.width <= Oval2.x + Oval2.width:
		# 	if Oval2.y <= Oval1.y <= Oval2.y+ Oval2.height or Oval2.y <= Oval1.y+Oval1.height <= Oval2.y+Oval2.height :
		# 		Oval1_vx = -Oval1_vx
		# if Oval2.y <= Oval1.y <= Oval2.y + Oval2.height or Oval2.y <= Oval1.y+Oval1.height <= Oval2.y+Oval2.height:
		# 	if Oval2.y <= Oval1.y >= Oval2.y + Oval2.width or Oval2.y <= Oval1.y + Oval1.height <= Oval2.y + Oval2.height:
		# 		Oval1_vy = -Oval1_vy

		# # 球二行為
		# if Oval2.x <= 0 or Oval2.x+Oval2.width >= window.width:
		# 	Oval2_vx = -Oval2_vx
		# if Oval2.y <= 0 or Oval2.y+Oval2.height >= window.height:
		# 	Oval2_vy = -Oval2_vy
		#球二碰撞檢測
		# if  Oval1.x <= Oval2.x <= Oval1.x + Oval1.width or Oval1.x <= Oval2.x+Oval2.width <= Oval1.x + Oval1.width:
		# 	if Oval1.y <= Oval2.y <= Oval1.y+ Oval1.height or Oval1.y <= Oval2.y+Oval2.height <= Oval1.y+Oval1.height :
		# 		Oval2_vx = -Oval2_vx
		# if Oval1.y <= Oval2.y <= Oval1.y + Oval1.height or Oval1.y <= Oval2.y+Oval2.height <= Oval1.y+Oval1.height:
		# 	if Oval1.y <= Oval2.y >= Oval1.y + Oval1.width or Oval1.y <= Oval2.y + Oval2.height <= Oval1.y + Oval1.height:
		# 		Oval2_vy = -Oval2_vy



		pause(10)
	pass


if __name__ == '__main__':
	main()

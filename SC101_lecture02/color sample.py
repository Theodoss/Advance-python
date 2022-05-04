from campy.graphics.gobjects import GOval,GRect,GPolygon,GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLine
from campy.graphics.gobjects import GLabel

window = GWindow(800, 400, title='color sample')

a_x = 20
a_y = 20
a_color = 'aliceblue'
a = GOval(20,20,x=a_x, y=a_y)
a.filled = True
a.fill_color = a_color
window.add(GLabel(a_color,a_x-10,a_y))
window.add(a)

b_x = 60
b_y = 20
b_color = 'antiquewhite'
b = GOval(20,20,x=b_x, y=b_y)
b.filled = True
b.fill_color = b_color
window.add(GLabel(b_color,b_x-10,b_y))
window.add(b)

a1_x = 100
a1_y = 20
a1_color = 'aqua'
a1 = GOval(20,20,x=a1_x, y=a1_y)
a1.filled = True
a1.fill_color = a1_color
window.add(GLabel(a1_color,a1_x-10,a1_y))
window.add(a1)

a2_x = 140
a2_y = 20
a2_color = 'aquamarine'
a2 = GOval(20,20,x=a2_x, y=a2_y)
a2.filled = True
a2.fill_color = a2_color
window.add(GLabel(a2_color,a2_x-10,a2_y))
window.add(a2)

a3_x = 200
a3_y = 20
a3_color = 'azure'
a3 = GOval(20,20,x=a3_x, y=a3_y)
a3.filled = True
a3.fill_color = a3_color
window.add(GLabel(a3_color,a3_x-10,a3_y))
window.add(a3)

a4_x = 200
a4_y = 20
a4_color = 'beige'
a4 = GOval(20,20,x=a4_x, y=a4_y)
a4.filled = True
a4.fill_color = a4_color
window.add(GLabel(a4_color,a4_x-10,a4_y))
window.add(a4)

# for
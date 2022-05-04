from campy.graphics.gobjects import GOval
from campy.graphics.gobjects import GRect
from campy.graphics.gobjects import GArc
from campy.graphics.gobjects import GLine
from campy.graphics.gobjects import GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow()
head = GPolygon()
head.add_vertex((100, 100))
head.add_vertex((200, 200))
head.add_vertex((100, 200))
head.add_vertex((300, 200))
head.filled= True
head.fill_color="blue"
head.color = "snow"
window.add(head)

body = GOval(200,200, x=200, y=200)
body.filled= True
body.fill_color="gold"
body.color = "gold"
window.add(body)



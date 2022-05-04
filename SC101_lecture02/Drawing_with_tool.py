"""
File: Draw_line.py
Name:
------------------------
This file shows how to use campy
mouse event to draw a line with two click
"""

from campy.graphics.gobjects import GOval,GArc,GPolygon,GRect,GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# This constant controls the size of the pen stroke
SIZE = 10

# Global variable 添加第一座標位置儲存器
hole_x = None
hole_y = None
window = GWindow(800, 400, title='Draw_line')
switch = False

polygon_switch = True
Line_switch = False
polygon_label = GLabel("Polygon_Tool", 10,290)
window.add(polygon_label)
line_label = GLabel("Line_Tool", 10,270)
window.add(line_label)

p_mouse_x =None
p_mouse_y =None
def main():
    # onmouseclicked(line_draw)  # 滑鼠監聽啟動
    onmouseclicked(polygon_draw)


def polygon_draw(mouse):
    global p_mouse_x
    global p_mouse_y
    global polygon_switch
    print("Layer 1")
    d = {}
    j = 1
    # for i in range(10):
    #     d['x'+str(i)]=i
    a = GPolygon()
    while polygon_switch is True:
        if mouse.x != p_mouse_x and mouse.y != p_mouse_y:
            a.add_vertex((mouse.x, mouse.y))
            p_mouse_x = mouse.x
            p_mouse_y = mouse.y
            print(mouse.x, mouse.y)
            pause(1000)
        if 10 < mouse.x <100 and 260 < mouse.y <400 :
            print("click switch")
            polygon_switch = False
    print("window add")
    window.add(a)

    # while True:
    #     print("layer 1")
    #     i = 1
    #     i = GPolygon()
    #     while polygon_switch is True:
    #         print("Layer 2")
    #         j = i.add_vertex(mouse.x, mouse.y)
    #         j += 1
    #         if 10 < mouse.x <60 and 260 < mouse.y <270 :
    #             polygon_switch = False
    #     window.add(i)
    #     i += 1



def line_draw(mouse):
    global hole_x
    global hole_y
    global switch

    if hole_x is None and switch is False:
        hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        print(GOval)
        window.add(hole)

    if hole_x is not None:  # 存在第一座標則劃線
        line = GLine(round(hole_x + (SIZE / 2)), round(hole_y + (SIZE / 2)), round(mouse.x + (SIZE / 2)),
                     round(mouse.y + (SIZE / 2)))
        window.add(line)
        switch = False
        print(f'{hole_x},{hole_y}::{mouse.x},{mouse.y}')
        window.add(GLabel(f'{hole_x},{hole_y}', hole_x-5, hole_y-5))
        window.add(GLabel(f'{mouse.x},{mouse.y}', mouse.x-5, mouse.y-5))
        if abs(mouse.x - hole_x) < 15:  # 避免產生勿刪除,設定斜率過高採用y邊抓取
            erase_hole1 = window.get_object_at(hole_x, hole_y + (SIZE / 2))
            # erase_hole2 = window.get_object_at(hole.x, hole.y + (SIZE / 2))
            # 刪除所有端點座標
            window.remove(erase_hole1)
            # window.remove(erase_hole2)
            hole_x, hole_y = (None, None)  # 將第一座標歸零
        else:  # 避免產生勿刪除,設定普通情況採用Ｘ邊抓取
            erase_hole1 = window.get_object_at(hole_x + (SIZE / 2), hole_y)
            # erase_hole2 = window.get_object_at(hole.x + (SIZE / 2), hole.y)
            # 刪除所有端點座標
            window.remove(erase_hole1)
            # window.remove(erase_hole2)
            hole_x, hole_y = (None, None)
    else:
        # 儲存為座標一
        hole_x = hole.x
        hole_y = hole.y
        switch = True

if __name__ == '__main__':
    main()
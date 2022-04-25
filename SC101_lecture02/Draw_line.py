"""
File: Draw_line.py
Name:
------------------------
This file shows how to use campy
mouse event to draw a line with two click
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLine

# This constant controls the size of the pen stroke
SIZE = 10
window = GWindow(200, 200,title = 'Draw_line')

#Global variable 添加第一座標位置儲存器
hole_x = None
hole_y = None

def main():
    onmouseclicked(click) #滑鼠監聽啟動

def click(mouse):
    global hole_x
    global hole_y
    hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
    window.add(hole)
    if hole_x is not None: #存在第一座標則劃線
        line = GLine(round(hole_x + (SIZE/2)), round(hole_y + (SIZE/2)), round(hole.x+ (SIZE/2)), round(hole.y+ (SIZE/2)))
        window.add(line)
        if abs(hole.x-hole_x)<15: #避免產生勿刪除,設定斜率過高採用y邊抓取
            erase_hole1 = window.get_object_at(hole_x, hole_y+ (SIZE/2))
            erase_hole2 = window.get_object_at(hole.x, hole.y+ (SIZE/2))
            #刪除所有端點座標
            window.remove(erase_hole1)
            window.remove(erase_hole2)
            hole_x, hole_y = (None,None) #將第一座標歸零
        else: #避免產生勿刪除,設定普通情況採用Ｘ邊抓取
            erase_hole1 = window.get_object_at(hole_x+ (SIZE/2), hole_y)
            erase_hole2 = window.get_object_at(hole.x+ (SIZE/2), hole.y)
            #刪除所有端點座標
            window.remove(erase_hole1)
            window.remove(erase_hole2)
            hole_x, hole_y = (None, None)
    else:
        #儲存為前一個
        hole_x = hole.x
        hole_y = hole.y


if __name__ == '__main__':
        main()

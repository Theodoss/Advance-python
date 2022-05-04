"""
File: Draw_line.py
Name:
------------------------
This file shows how to use campy
mouse event to draw a line with two click
"""

from campy.graphics.gobjects import GOval,GRect,GPolygon,GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLine
from campy.graphics.gobjects import GLabel

# This constant controls the size of the pen stroke
SIZE = 10

# Global variable 添加第一座標位置儲存器
hole_x = None
hole_y = None
switch = False

window = GWindow(800, 400, title='Draw_line')

body = GPolygon()
body.add_vertex((290,235))
body.add_vertex((278,294))
body.add_vertex((283,402))
body.add_vertex((480,402))
body.add_vertex((485,315))
body.add_vertex((465,235))
body.filled = True
body.color = "gold"
body.fill_color = "gold"
window.add(body)

head = GPolygon()
head.add_vertex((310,123))
head.add_vertex((450,125))
head.add_vertex((473,212))
head.add_vertex((279,223))
head.filled = True
head.color = "gold"
head.fill_color = "gold"
window.add(head)

#Mark for jaw
jaw = GOval(195,60,x=280, y=190)
jaw.filled = True
jaw.color = "gold"
jaw.fill_color = "gold"
window.add(jaw)

fore_head = GOval(140,55,x=310, y=100)
fore_head.filled = True
fore_head.color = "gold"
fore_head.fill_color = "gold"
window.add(fore_head)

ear1 = GPolygon()
ear1.add_vertex((305,137))
ear1.add_vertex((259,117))
ear1.add_vertex((232,103))
ear1.add_vertex((210,86))
ear1.add_vertex((193,57))
ear1.add_vertex((230,50))
ear1.add_vertex((265,66))
ear1.add_vertex((289,80))
ear1.add_vertex((313,94))
ear1.add_vertex((328,110))
ear1.filled = True
ear1.color = "goldenrod"
ear1.fill_color = "goldenrod"
window.add(ear1)

ear1_shadow = GPolygon()
ear1_shadow.add_vertex((232,103))
ear1_shadow.add_vertex((210,86))
ear1_shadow.add_vertex((193,57))
ear1_shadow.add_vertex((230,50))
ear1_shadow.filled = True
ear1_shadow.color = "black"
ear1_shadow.fill_color = "black"
window.add(ear1_shadow)

ear2 = GPolygon()
ear2.add_vertex((426,107))
ear2.add_vertex((446,76))
ear2.add_vertex((467,54))
ear2.add_vertex((501,35))
ear2.add_vertex((530,30))
ear2.add_vertex((535,60))
ear2.add_vertex((488,99))
ear2.add_vertex((445,119))
ear2.filled = True
ear2.color = "goldenrod"
ear2.fill_color = "goldenrod"
window.add(ear2)

ear2_shadow = GPolygon()

ear2_shadow.add_vertex((501,35))
ear2_shadow.add_vertex((530,30))
ear2_shadow.add_vertex((535,60))
ear2_shadow.add_vertex((488,99))
ear2_shadow.filled = True
ear2_shadow.color = "black"
ear2_shadow.fill_color = "black"
window.add(ear2_shadow)

arm_arc1 = GArc(200, 800, 20, 60, x=280, y=300)
arm_arc1.color = "black"
window.add(arm_arc1)

armR_shadow = GPolygon()
armR_shadow.add_vertex((292,375))
armR_shadow.add_vertex((303,393))
armR_shadow.add_vertex((303,400))
armR_shadow.add_vertex((297,403))
armR_shadow.filled = True
armR_shadow.color = "brown"
armR_shadow.fill_color = "brown"
window.add(armR_shadow)

arm_arc2 = GArc(200, 250, 180, 60, x=293, y=300)
arm_arc2.color = "black"
window.add(arm_arc2)

arm_acr3 = GArc(200, 800, 110, 60, x=420, y=280)
arm_acr3.color = "black"
window.add(arm_acr3)

arm_acr4 = GArc(200, 300, 270, 80, x=380, y=290)
arm_acr4.color = "black"
window.add(arm_acr4)

armL_shadow = GPolygon()
armL_shadow.add_vertex((292,375))
armL_shadow.add_vertex((303,393))
armL_shadow.add_vertex((303,400))
armL_shadow.add_vertex((297,403))
armL_shadow.filled = True
armL_shadow.color = "brown"
armL_shadow.fill_color = "brown"
window.add(armL_shadow)

tail = GPolygon()
tail.add_vertex((481,376))
tail.add_vertex((512,379))
tail.add_vertex((500,307))
tail.add_vertex((551,296))
tail.add_vertex((511,176))
tail.add_vertex((745,136))
tail.add_vertex((720,285))
tail.add_vertex((611,256))
tail.add_vertex((628,355))
tail.add_vertex((551,344))
tail.add_vertex((555,400))
tail.add_vertex((478,400))
tail.filled = True
tail.color = "gold"
tail.fill_color = "gold"
window.add(tail)

tail_shadow = GPolygon()
tail_shadow.add_vertex((481,376))
tail_shadow.add_vertex((512,379))
tail_shadow.add_vertex((508,355))
tail_shadow.add_vertex((515,348))
tail_shadow.add_vertex((523,363))
tail_shadow.add_vertex((533,355))
tail_shadow.add_vertex((539,360))
tail_shadow.add_vertex((544,355))
tail_shadow.add_vertex((552,360))

tail_shadow.add_vertex((555,400))
tail_shadow.add_vertex((478,400))
tail_shadow.filled = True
tail_shadow.color = "brown"
tail_shadow.fill_color = "brown"
window.add(tail_shadow)

chickR = GOval(40,50,x=285,y=180)
chickR.filled = True
chickR.color = "red"
chickR.fill_color = "red"
window.add(chickR)

chickL = GOval(40,50,x=430,y=180)
chickL.filled = True
chickL.color = "red"
chickL.fill_color = "red"
window.add(chickL)

noise = GArc(10,12, 180, 180, x=375, y=183)
noise.filled = True
noise.color = "black"
noise.fill_color = "black"
window.add(noise)

mouse1 = GArc(20,20, 180, 150, x=355, y=203)
mouse1.color = "black"
mouse1.fill_color = "black"
window.add(mouse1)

mouse2 = GArc(20,20, 0, 180, x=373, y=206)
mouse2.color = "black"
mouse2.fill_color = "black"
window.add(mouse2)

mouse3 = GArc(20,20, 190, 190, x=393, y=202)
mouse3.color = "black"
mouse3.fill_color = "black"
window.add(mouse3)

eye1 = GOval(30,30, x=313, y=153)
eye1.filled = True
eye1.color = "black"
eye1.fill_color = "black"
window.add(eye1)

eyeball1 = GOval(10,10, x=328, y=158)
eyeball1.filled = True
eyeball1.color = "snow"
eyeball1.fill_color = "snow"
window.add(eyeball1)

eye2 = GOval(30,30, x=408, y=153)
eye2.filled = True
eye2.color = "black"
eye2.fill_color = "black"
window.add(eye2)

eyeball2 = GOval(10,10, x=412, y=158)
eyeball2.filled = True
eyeball2.color = "snow"
eyeball2.fill_color = "snow"
window.add(eyeball2)

jaw_shadow3 = GArc(80, 60, 180, 180, x=355, y=238)
jaw_shadow3.filled = True
jaw_shadow3.color = "brown"
jaw_shadow3.fill_color = "brown"
window.add(jaw_shadow3)

jaw_shadow2 = GArc(130, 50, 180, 180, x=312, y=235)
jaw_shadow2.filled = True
jaw_shadow2.color = "goldenrod"
jaw_shadow2.fill_color = "goldenrod"
window.add(jaw_shadow2)

jaw_shadow = GArc(130, 40, 180, 180, x=312, y=232)
jaw_shadow.filled = True
jaw_shadow.color = "gold"
jaw_shadow.fill_color = "gold"
window.add(jaw_shadow)





def main():
    onmouseclicked(click)  # 滑鼠監聽啟動


def click(mouse):
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
        label = GLabel(f'{hole_x + (SIZE / 2)},{hole_y + (SIZE / 2)}',hole_x,hole_y-20)
        window.add(label)
        label2 = GLabel(f'{mouse.x + (SIZE / 2)},{mouse.y + (SIZE / 2)}', mouse.x, mouse.y-20)
        window.add(label2)
        print(f'{hole_x + (SIZE / 2)},{hole_y + (SIZE / 2)}----{mouse.x + (SIZE / 2)},{mouse.y + (SIZE / 2)}')
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

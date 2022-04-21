"""
File: my_drawing.py
Name: 
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect,GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width= 800, height= 500, title = 'Draw1')
    face = GOval(300, 200, x=400, y=250,)
    face.filled = True
    face.fill_color ='red'
    l_eye = GOval(100, 100, x=400, y=250)
    r_eye= GOval(100, 100, x=300, y=250)
    mouth = GRect(300, 200, x=100, y=0)
    mouth.filled = True
    mouth.fill_color ='blue'
    label = GLabel('Hellow, World!', x=200, y=250)
    label.font= '-80'
    label.color = 'yellow'


    list = [face, l_eye, r_eye, mouth, label]
    for i in list:
        window.add(i)

    pass


if __name__ == '__main__':
    main()

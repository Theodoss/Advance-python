"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

# Global variables
# TODO:
score = 0
label = GLabel('Score==='+str(score) )
def main():
    label.font = '-30'
    window.add(label,0 ,label.height )
    onmouseclicked(remove_mole)
    while True:
        img = GImage('mole.png')
        random_x = random.randint(0, WINDOW_WIDTH-img.width)
        random_y = random.randint(0, WINDOW_HEIGHT-img.height)
        window.add(img, random_x, random_y)

        pause(DELAY)

def remove_mole(event):
    maybe_mole = window.get_object_at(event.x, event.y)
    if maybe_mole is not None and maybe_mole is not label:
        window.remove(maybe_mole)
        global score
        score +=1
        label.text ='Scroe==='+str(score)

if __name__ == '__main__':
    main()

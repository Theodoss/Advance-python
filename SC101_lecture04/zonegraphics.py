from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self._ball = None
        self._window = GWindow(width=window_width, height=window_height)
        # Create zone
        self._zone = GRect(zone_width, zone_height)
        self._zone.color = 'red'
        self._window.add(self._zone, (window_width - zone_width) / 2, (window_height - zone_height) / 2)
        # Create ball and initialize velocity/position
        self._ball = GOval(ball_radius * 2, ball_radius * 2)
        self._ball.filled = True
        self._ball.color = 'blue'
        self._ball.fill_color = 'blue'
        self._window.add(self._ball)
        self.vx = 1
        self.vy = 1
        self.reset_ball()

        onmouseclicked(self.click)

        # Initialize mouse listeners

    def click(self, event):
        obj = self._window.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.reset_ball()

    def set_ball_position(self):
        random_x = random.randint(0, self._window.width - self._ball.width)
        random_y = random.randint(0, self._window.height - self._ball.height)
        if (self._window.width - self._zone.width) / 2 < random_x < (self._window.width + self._zone.width) / 2 \
                and (self._window.height - self._zone.height) / 2 < random_y < (
                self._window.height + self._zone.height) / 2:
            return None
        else:
            self._ball.x = random_x
            self._ball.y = random_y

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
            self._window.add(self._ball)

    def ball_in_zone(self):
        zone_left_side = self._zone.x
        zone_right_side = self._zone.x + self._zone.width
        is_ball_in_zone = zone_left_side <= self._ball.x <= zone_right_side
        zone_top_side = self._zone.y
        zone_bottom_side = self._zone.y + self._zone.height
        is_ball_y_in_zone = zone_top_side <= self._ball.x <= zone_bottom_side
        return is_ball_in_zone and is_ball_y_in_zone

    def set_ball_velocity(self):
        self.vx = random.randint(0, MAX_SPEED)
        self.vy = random.randint(MIN_Y_SPEED, MIN_Y_SPEED)
        if random.random() > 0.5:
            self.vx = - self.vx
        if random.random() > 0.5:
            self.vy = - self.vy

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def set_vx(self):
        self.vx *= -1

    def set_vy(self):
        self.vy *= -1

    @property
    def ball(self):
        return self._ball

import pyautogui
import time


class AutoClicker:
    def __init__(self, time_lap, pos_x=None, pos_y=None):
        self.time_lap = time_lap
        self.pos_x = pos_x
        self.pos_y = pos_y

    def run(self):
        count = 0

        if self.pos_x is None and self.pos_y is None:
            self.pos_x, self.pos_y = pyautogui.position()

        while True:
            pyautogui.click(clicks=1)

            print("Click :::", count)
            count += 1

            time.sleep(self.time_lap)

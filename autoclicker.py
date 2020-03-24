import pyautogui
import time
import sys


class AutoClicker:
    """The AutoClicker class, defines the autoclicking
    programm on the mouse, used the pyautogui and time library.

    Attributes:
        time_lap, pos_x, pos_y, clicks, button, times.

    Methodes:
        __init__
        click
        setMousePosition
        runEnd
        runEndless
    """

    def __init__(self, time_lap=0, pos_x=None, pos_y=None, clicks=1,
                 button=pyautogui.LEFT, times=None):
        """This is the initialisation method:
        the definition of the variables are below.

        self.time_lap = time_lap    # the time lap, between each click
        self.pos_x = pos_x          # the x posistion of the mouse
        self.pos_y = pos_y          # the y posistion of the mouse
        self.clicks = clicks        # the number of clicke, per time
        self.button = button        # the clicked button, either left or right
        self.times = times          # how many times, to do the clicks

        time_lap, is in Secondes
        self.pos_x and self.pos_y, are integers but None by default
                                    for current curssor position
        self.clicks, integer it takes 1 by default, but in general
                    it takes(1,2)
        self.times, integer but None by default for no stop clicking.
        self.screen_width            # screen, monitor's width
        self.screen_height           # screen, monitor's height
        """
        self.time_lap = time_lap    # the time lap, between each click
        self.pos_x = pos_x          # the x posistion of the mouse
        self.pos_y = pos_y          # the y posistion of the mouse
        self.clicks = clicks        # the number of clicke, per time
        self.button = button        # the clicked button, either left or right
        self.times = times          # how many times, to do the clicks
        self.screen_width, self.screen_height = pyautogui.size()    # abvious

    def click(self):
        """This method defines a single click event of the mouse."""
        pyautogui.click(clicks=self.clicks, button=self.button)

    def setMousePosition(self):
        """This method, defines the mouse's cursor position.
        In case the user doesn't specify the positions,
        use the default position, of where the mouse is.
        """
        if self.pos_x is None and self.pos_y is None:
            self.pos_x, self.pos_y = pyautogui.position()
        else:
            # in case the mouse cursor position is out of boubds
            cond1 = (0 <= self.pos_x <= self.screen_width)
            cond2 = (0 <= self.pos_y <= self.screen_height)

            # if so, exit the execution witha notification error
            if cond1 or cond2:
                raise ValueError('Mouse cursor: pox_x & pos_y out of bounds.')

                sys.exit()

    def runEndless(self):
        """FOR ENDLESS ITERATIONS, UNKOWN TIMES OF ITERATIONS.
        This is the run method it defines the all programm.
        from clicking, to time sleeping.
        """
        self.setMousePosition()             # setting the possition

        while True:
            self.click()                    # on click event
            time.sleep(self.time_lap)       # sleeping

    def runEnd(self):
        """FOR A KNOWN NUMBER OF TIMES.
        This is the run method it defines the all programm.
        from clicking, to time sleeping.
        """
        self.setMousePosition()             # setting the possition

        for count in range(self.times):
            self.click()                    # on click event
            time.sleep(self.time_lap)       # sleeping

    def start(self):
        """For telling the autoClicker to start."""
        if self.times is None:
            self.runEndless()
        else:
            self.runEnd()


if __name__ == "__main__":
    clicker = AutoClicker(time_lap=3, times=10)
    clicker.start()

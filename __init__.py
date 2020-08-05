from autoclicker import AutoClicker

# declaring, see autoclicker.py and read the documentation
clicker = AutoClicker(time_lap=2, times=10)
clicker = AutoClicker(time_lap=10, times=None, clicks=1, button='right',
                      pos_x=123, pos_y=444)
clicker = AutoClicker(clicks=2, button='left')

# start the autoclicker
clicker.start()

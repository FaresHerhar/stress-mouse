import keyboard

START = "Ctrl + Shift + F5"         # starting keyboard shortcut
STOP = "Ctrl + Shift + F6"         # pausing keyboard shortcut
PAUSE = "Ctrl + Shift + F7"          # stoping keyboard shortcut


def start():
    print("STARTING")


def stop():
    print("STOPING")


def pause():
    while not keyboard.is_pressed("l"):
        print("PAUSING")


keyboard.add_hotkey(START, start)
keyboard.add_hotkey(STOP, stop)
keyboard.add_hotkey(PAUSE, pause)

was = False

while not keyboard.is_pressed("ESC"):
    pass

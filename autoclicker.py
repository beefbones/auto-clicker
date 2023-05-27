import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay_time = 0.5
button_direction = Button.right
start_stop_button = KeyCode(char='a')
terminate_button = KeyCode(char='b')

class ClickTheMouse(threading.Thread):
    def __init__(self, delay_time, button_direction):
        super().__init__()
        self.delay_time = delay_time
        self.button_direction = button_direction
        self.running = False
        self.program_running = True

    def start_mouse_click(self):
        self.running = True

    def stop_mouse_click(self):
        self.running = False

    def exit_script(self):
        self.stop_mouse_click()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button_direction)
                time.sleep(self.delay_time)
                time.sleep(0.1)

mouse = Controller()
click_thread = ClickTheMouse(delay_time, button_direction)
click_thread.start()

def on_press(key):
    if key == start_stop_button:
        if click_thread.running:
            click_thread.stop_mouse_click()
        else:
            click_thread.start_mouse_click()
    elif key == terminate_button:
        click_thread.exit_script()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

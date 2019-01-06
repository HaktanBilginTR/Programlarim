from pynput.keyboard import Key, Listener
evennts = []
def on_press(Key):
    key_press = Key
    evennts.append(key_press)
with Listener(on_press=on_press) as listener:
    listener.join()
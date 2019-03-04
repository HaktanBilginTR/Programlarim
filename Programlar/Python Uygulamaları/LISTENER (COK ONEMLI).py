from pynput.keyboard import Key, Listener
evennts = []


def on_press(Key):
    key_press = Key
    evennts.append(key_press)
    if str(Key) == "'a'":
        return print("anne")
    elif str(Key) == "'b'":
        return print("baba")
    return print("haha")


with Listener(on_press=on_press) as listener:
    listener.join()

import keyboard


def space_pressed():
    print("Space was pressed!")


def up_pressed():
    print("GO up")
global i
i = 0
def add(i):
    i += 1
    return i
i = add(i)



# register the hotkey using the keyboard library
keyboard.add_hotkey('space', space_pressed)
keyboard.add_hotkey('w', add)


print(i)

# wait for keyboard events
keyboard.wait()
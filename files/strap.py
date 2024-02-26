# ducky files
for i in ["ducky.lja", "duckyline.lja", "duckycat.lja"]:
    shutil.copy(i, path.join(root, "bin", i))

try:
    mkdir(path.join(root, "bin/ducky"))
except FileExistsError:
    pass
for i in [
    "ducky.py",
    "duckyline.py",
    "duckyload.py",
    "duckycat.py",
]:
    shutil.copy(i, path.join(root, "bin/ducky", i))

shutil.copy("help_ducky.txt", path.join(root, "usr/share/help", "ducky.txt"))
shutil.copy("help_duckyline.txt", path.join(root, "usr/share/help", "duckyline.txt"))
shutil.copy("help_duckycat.txt", path.join(root, "usr/share/help", "duckycat.txt"))

# hid files
try:
    mkdir(path.join(root, "lib/adafruit_hid"))
except FileExistsError:
    pass

for i in [
    "__init__.mpy",
    "consumer_control_code.mpy",
    "consumer_control.mpy",
    "keyboard_layout_base.mpy",
    "keyboard_layout_us.mpy",
    "keyboard.mpy",
    "keycode.mpy",
    "mouse.mpy",
]:
    shutil.copy(i, path.join(root, "lib/adafruit_hid", i))

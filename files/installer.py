# ducky files
for pv[get_pid()]["filee"] in ["ducky.lja", "duckyline.lja", "duckycat.lja"]:
    ljinux.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))

ljinux.based.run("mkdir /bin/ducky")
for pv[get_pid()]["filee"] in [
    "ducky.py",
    "duckyline.py",
    "duckyload.py",
    "duckycat.py",
]:
    ljinux.based.run("cp " + vr("filee") + " /bin/ducky/" + vr("filee"))

ljinux.based.run("cp help_ducky.txt /usr/share/help/ducky.txt")
ljinux.based.run("cp help_duckyline.txt /usr/share/help/duckyline.txt")
ljinux.based.run("cp help_duckycat.txt /usr/share/help/duckycat.txt")

# hid files
ljinux.based.run("mkdir /lib/adafruit_hid")

for pv[get_pid()]["filee"] in [
    "__init__.mpy",
    "consumer_control_code.mpy",
    "consumer_control.mpy",
    "keyboard_layout_base.mpy",
    "keyboard_layout_us.mpy",
    "keyboard.mpy",
    "keycode.mpy",
    "mouse.mpy",
]:
    ljinux.based.run("cp " + vr("filee") + " /lib/adafruit_hid/" + vr("filee"))

ljinux.api.setvar("return", "0")

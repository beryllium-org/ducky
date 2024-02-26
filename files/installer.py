# ducky files
for pv[get_pid()]["filee"] in ["ducky.lja", "duckyline.lja", "duckycat.lja"]:
    be.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))

be.based.run("mkdir /bin/ducky")
for pv[get_pid()]["filee"] in [
    "ducky.py",
    "duckyline.py",
    "duckyload.py",
    "duckycat.py",
]:
    be.based.run("cp " + vr("filee") + " /bin/ducky/" + vr("filee"))

be.based.run("cp help_ducky.txt /usr/share/help/ducky.txt")
be.based.run("cp help_duckyline.txt /usr/share/help/duckyline.txt")
be.based.run("cp help_duckycat.txt /usr/share/help/duckycat.txt")

# hid files
be.based.run("mkdir /lib/adafruit_hid")

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
    be.based.run("cp " + vr("filee") + " /lib/adafruit_hid/" + vr("filee"))

be.api.setvar("return", "0")

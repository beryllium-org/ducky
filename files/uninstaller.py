be.based.run(
    "rm /lib/adafruit_hid/__init__.mpy /lib/adafruit_hid/consumer_control_code.mpy /lib/adafruit_hid/consumer_control.mpy /lib/adafruit_hid/keyboard_layout_base.mpy /lib/adafruit_hid/keyboard_layout_us.mpy /lib/adafruit_hid/keyboard.mpy /lib/adafruit_hid/keycode.mpy /lib/adafruit_hid/mouse.mpy /bin/ducky.lja /bin/duckyline.lja /bin/duckycat.lja /bin/ducky/ducky.py /bin/ducky/duckyline.py /bin/ducky/duckycat.py /bin/ducky/duckyload.py /usr/share/help/ducky.txt /usr/share/help/duckyline.txt /usr/share/help/duckycat.txt",
)
be.based.run("rmdir /lib/adafruit_hid")
be.based.run("rmdir /bin/ducky")
be.api.setvar("return", "0")

ljinux.based.run("rm &/lib/adafruit_hid/__init__.mpy &/lib/adafruit_hid/consumer_control_code.mpy &/lib/adafruit_hid/consumer_control.mpy &/lib/adafruit_hid/keyboard_layout_base.mpy &/lib/adafruit_hid/keyboard_layout_us.mpy &/lib/adafruit_hid/keyboard.mpy &/lib/adafruit_hid/keycode.mpy &/lib/adafruit_hid/mouse.mpy /bin/ducky.lja /bin/ducky.py /bin/duckyline.lja /bin/duckyline.py")

ljinux.based.run("rmdir &/lib/adafruit_hid")

ljinux.api.setvar("return", "0")

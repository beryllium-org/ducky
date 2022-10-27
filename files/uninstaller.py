# ducky files
ljinux.api.var(
    "argj", "a /bin/ducky.lja /bin/ducky.py /bin/duckyline.lja /bin/duckyline.py"
)
ljinux.based.command.fpexecc([None, "/bin/rm.py"])

# hid files
ljinux.api.var(
    "argj",
    "a &/lib/adafruit_hid/__init__.mpy &/lib/adafruit_hid/consumer_control_code.mpy &/lib/adafruit_hid/consumer_control.mpy &/lib/adafruit_hid/keyboard_layout_base.mpy &/lib/adafruit_hid/keyboard_layout_us.mpy &/lib/adafruit_hid/keyboard.mpy &/lib/adafruit_hid/keycode.mpy &/lib/adafruit_hid/mouse.mpy",
)
ljinux.based.command.fpexecc([None, "/bin/rm.py"])

ljinux.api.var("argj", "a &/lib/adafruit_hid")
ljinux.based.command.fpexecc([None, "/bin/rmdir.py"])

ljinux.api.var("return", "0")

# ducky files
ljinux.api.setvar(
    "argj", "a /bin/ducky.lja /bin/ducky.py /bin/duckyline.lja /bin/duckyline.py"
)
ljinux.based.command.fpexec("/bin/rm.py")

# hid files
ljinux.api.setvar(
    "argj",
    "a &/lib/adafruit_hid/__init__.mpy &/lib/adafruit_hid/consumer_control_code.mpy &/lib/adafruit_hid/consumer_control.mpy &/lib/adafruit_hid/keyboard_layout_base.mpy &/lib/adafruit_hid/keyboard_layout_us.mpy &/lib/adafruit_hid/keyboard.mpy &/lib/adafruit_hid/keycode.mpy &/lib/adafruit_hid/mouse.mpy",
)
ljinux.based.command.fpexec("/bin/rm.py")

ljinux.api.setvar("argj", "a &/lib/adafruit_hid")
ljinux.based.command.fpexec("/bin/rmdir.py")

ljinux.api.setvar("return", "0")

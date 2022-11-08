# ducky files

for filee in ["ducky.lja", "ducky.py", "duckyline.lja", "duckyline.py"]:
    ljinux.api.setvar("argj", f"cp {filee} /bin/{filee}")
    ljinux.based.command.fpexec("/bin/cp.py")
    del filee

# hid files
ljinux.api.setvar("argj", f"mkdir &/lib/adafruit_hid")
ljinux.based.command.fpexec("/bin/mkdir.py")

for filee in [
    "__init__.mpy",
    "consumer_control_code.mpy",
    "consumer_control.mpy",
    "keyboard_layout_base.mpy",
    "keyboard_layout_us.mpy",
    "keyboard.mpy",
    "keycode.mpy",
    "mouse.mpy",
]:
    ljinux.api.setvar("argj", f"cp {filee} &/lib/adafruit_hid/{filee}")
    ljinux.based.command.fpexec("/bin/cp.py")

ljinux.api.setvar("return", "0")

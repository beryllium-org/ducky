# ducky files
for filee in ["ducky.lja", "ducky.py", "duckyline.lja", "duckyline.py"]:
    ljinux.based.run(f"cp {filee} /bin/{filee}")
    del filee

# hid files
ljinux.based.run("mkdir &/lib/adafruit_hid")

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
    ljinux.based.run(f"cp {filee} &/lib/adafruit_hid/{filee}")

ljinux.api.setvar("return", "0")

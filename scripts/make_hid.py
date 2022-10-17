from platform import uname
from os import listdir, system

def errexit():
    print("Compilation error, exiting")
    exit(1)

mpyn = f"./scripts/mpy-cross-{uname().machine}"
path = "./submodules/Adafruit_CircuitPython_HID/adafruit_hid/"

print(f"Compiling Adafruit_HID..\nUsing mpycross: {mpyn}\n")

for filee in listdir(path):
    a = system(
        f"{mpyn} {path}{filee} -s {filee[:-3]} -v -O4 -o ./files/{filee[:-3]}.mpy"
    )
    print(f"{filee} -> {filee[:-3]}.mpy")

    if a != 0:
        errexit()

print()

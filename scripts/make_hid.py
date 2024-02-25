from os import listdir, system
from sys import path as spath


def errexit():
    print("Compilation error, exiting")
    exit(1)


spath.append("./submodules/CircuitMPY/")
import circuitmpy

circuitmpy.fetch_mpy()
path = "./submodules/Adafruit_CircuitPython_HID/adafruit_hid/"

for filee in listdir(path):
    try:
        print(f"{filee} -> {filee[:-3]}.mpy")
        circuitmpy.compile_mpy(f"{path}{filee}", f"./files/{filee[:-3]}.mpy")
    except:
        errexit()

print()

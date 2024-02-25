rename_process("ducky")
if cptoml.fetch("usb_hid_available", "LJINUX"):
    if cptoml.fetch("usb_hid_enabled", "LJINUX"):
        ljinux.api.subscript("/bin/ducky/duckyload.py")
    else:
        term.write(
            "usb_hid is not enabled in `&/settings.toml`!\n"
            + "To enable it, set `usb_hid_enabled` to 'true'."
        )
else:
    term.write("This board does not support usb_hid!")
try:
    vr("opts", ljinux.api.xarg())
    if "h" in vr("opts")["o"] or "help" in vr("opts")["o"]:
        ljinux.based.run("cat /")
    else:
        if len(vr("opts")["w"]):
            pass
        else:
            pass
    if ljinux.api.isdir(ljinux.based.user_vars["argj"].split()[1], rdir=getcwd()):
        ljinux.based.error(4, ljinux.based.user_vars["argj"].split()[1])
        ljinux.based.user_vars["return"] = "1"
    else:
        with open(
            ljinux.api.betterpath(ljinux.based.user_vars["argj"].split()[1]), "r"
        ) as f:
            dataa = f.readlines()

        lc = len(dataa)
        cl = 0

        for i in range(0, lc):
            dataa[i] = dataa[i].replace("\n", "")

        ljinux.based.user_vars["return"] = "0"
        while cl != lc:
            line = dataa[cl]
            print(line)
            cmd = (
                line[: line.find(" ", 0)].upper()
                if line.find(" ", 0) != -1
                else line.upper()
            )
            args = line[line.find(" ", 0) + 1 :]
            del line
            if cmd.upper() == "DELAY":
                sleep(float(args) / 1000)
            elif cmd == "STRING":
                layout.write(args)
            elif cmd == "REM":
                pass
            elif cmd in ["DEFAULT_DELAY", "DEFAULTDELAY"]:
                defaultDelay = int(line[13:]) * 10
            elif cmd in duckyCommands:
                stack = [cmd] + args.split()
                for i in stack:
                    if i.upper() in duckyCommands:
                        kbd.press(duckyCommands[i.upper()])
                    else:
                        print(f'Error: Key "{i}" not found')
                        ljinux.based.user_vars["return"] = "1"
                        break
                del stack
                kbd.release_all()
            elif cmd == "REPEAT":
                cl -= 2
            else:
                print(f'Error: Command "{cmd}" not found')
                ljinux.based.user_vars["return"] = "1"
                break
            sleep(defaultDelay / 1000)
            del cmd, args
            cl += 1
        del duckyCommands, dataa, lc, cl, kbd, layout
        del KeyboardLayoutUS, Keycode, defaultDelay
except IndexError:
    ljinux.based.error(1)

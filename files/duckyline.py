rename_process("duckyline")
vr("opts", ljinux.api.xarg())
if "h" in vr("opts")["o"] or "help" in vr("opts")["o"]:
    ljinux.based.run("cat /usr/share/help/duckyline.txt")
else:
    if cptoml.fetch("usb_hid_available", "LJINUX"):
        if cptoml.fetch("usb_hid_enabled", "LJINUX"):
            if len(vr("opts")["w"]):
                ljinux.api.setvar("return", "0")
                ljinux.api.subscript("/bin/ducky/duckyload.py")
                if vr("success"):
                    if vr("opts")["w"][0].upper() == "STRING":
                        vr("layout").write("".join(vr("opts")["w"][1:]))
                    elif vr("opts")["w"][0].upper() in vr("duckyCommands"):
                        for pv[get_pid()]["i"] in vr("opts")["w"]:
                            if vr("i").upper() in vr("duckyCommands"):
                                vr("kbd").press(vr("duckyCommands")[vr("i").upper()])
                            else:
                                term.write(
                                    'Error: Command "' + vr("i") + '" not found!'
                                )
                                ljinux.api.setvar("return", "1")
                                vr("kbd").release_all()
                        vr("kbd").release_all()
                    else:
                        term.write("This command isn't supported by duckyline!")
                        ljinux.api.setvar("return", "1")
                    del Keyboard, KeyboardLayoutUS, Keycode
                else:
                    term.write("Failed to initialize usb_hid!")
            else:
                term.write(
                    "usb_hid is not enabled in `&/settings.toml`!\n"
                    + "To enable it, set `usb_hid_enabled` to 'true' and reboot."
                )
    else:
        term.write("This board does not support usb_hid!")

rename_process("duckycat")
vr("opts", ljinux.api.xarg())
if "h" in vr("opts")["o"] or "help" in vr("opts")["o"]:
    ljinux.based.run("cat /usr/share/help/duckycat.txt")
else:
    if cptoml.fetch("usb_hid_available", "LJINUX"):
        if cptoml.fetch("usb_hid_enabled", "LJINUX"):
            if len(vr("opts")["w"]):
                ljinux.api.setvar("return", "0")
                ljinux.api.subscript("/bin/ducky/duckyload.py")
                if vr("success"):
                    with ljinux.api.fopen(vr("opts")["w"][0]) as pv[get_pid()]["file"]:
                        if vr("file") is not None:
                            vr("lines", vr("file").readlines())
                            vr("lc", len(vr("lines")))
                            for pv[get_pid()]["i"] in range(vr("lc")):
                                term.clear_line()
                                term.nwrite(
                                    "Writing.. ("
                                    + str(vr("i") + 1)
                                    + "/"
                                    + str(vr("lc"))
                                    + ")"
                                )
                                vr("layout").write(vr("lines")[vr("i")])
                            term.write()
                        else:
                            ljinux.based.error(
                                4,
                                f=vr("opts")["w"][0],
                                prefix=f"{colors.blue_t}duckycat{colors.endc}",
                            )
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

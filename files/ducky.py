rename_process("ducky")
vr("opts", be.api.xarg())
if "h" in vr("opts")["o"] or "help" in vr("opts")["o"]:
    be.based.run("cat /usr/share/help/ducky.txt")
else:
    if cptoml.fetch("usb_hid_available", "BERYLLIUM"):
        if cptoml.fetch("usb_hid_enabled", "BERYLLIUM"):
            if len(vr("opts")["w"]):
                be.api.setvar("return", "1")
                with be.api.fopen(vr("opts")["w"][0]) as pv[get_pid()]["script"]:
                    if vr("script") is not None:
                        vr("cmds", vr("script").readlines())
                        vr("lc", len(vr("cmds")))
                        for pv[get_pid()]["i"] in range(vr("lc")):
                            vr("cmds")[vr("i")] = vr("cmds")[vr("i")].replace("\n", "")
                        be.api.subscript("/bin/ducky/duckyload.py")
                        if vr("success"):
                            vr("cl", 0)
                            vr("nrepeat", False)
                            be.api.setvar("return", "0")
                            while vr("cl") != vr("lc"):
                                vr("line", vr("cmds")[vr("cl")])
                                term.write(vr("line"))
                                vr("lsps", vr("line").find(" "))
                                vr("args", None)
                                if vr("lsps") != -1:
                                    vr("cmd", vr("line")[: vr("lsps")])
                                    vr("args", vr("line")[vr("lsps") + 1 :])
                                else:
                                    vr("cmd", vr("line"))
                                vr("cmd", vr("cmd").upper())
                                if vr("cmd") == "DELAY":
                                    try:
                                        sleep(float(vr("args")) / 1000)
                                    except ValueError:
                                        term.write("Invalid time period specified!")
                                        be.api.setvar("return", "1")
                                        break
                                elif vr("cmd") == "STRING":
                                    vr("layout").write(vr("args"))
                                elif vr("cmd") == "REM":
                                    pass
                                elif vr("cmd") in ["DEFAULT_DELAY", "DEFAULTDELAY"]:
                                    vr("defaultDelay", int(vr("args")))
                                elif vr("cmd") in vr("duckyCommands"):
                                    vr("cmdl", vr("line").upper().split(" "))
                                    for pv[get_pid()]["i"] in vr("cmdl"):
                                        if vr("i") in vr("duckyCommands"):
                                            vr("kbd").press(
                                                vr("duckyCommands")[vr("i")]
                                            )
                                        else:
                                            term.write(
                                                'Error: Command "'
                                                + vr("i")
                                                + '" not found!'
                                            )
                                            be.api.setvar("return", "1")
                                            vr("kbd").release_all()
                                            break
                                    vr("kbd").release_all()
                                elif vr("cmd") == "REPEAT":
                                    if vr("nrepeat"):
                                        vr("nrepeat", False)
                                        term.write("*ignored*")
                                    else:
                                        vrm("cl", 2)
                                        vr("nrepeat", True)
                                else:
                                    term.write(
                                        'Error: Command "' + vr("cmd") + '" not found!'
                                    )
                                    be.api.setvar("return", "1")
                                    break
                                vrp("cl")
                                sleep(vr("defaultDelay") / 1000)
                            del Keyboard, KeyboardLayoutUS, Keycode
                        else:
                            term.write("Failed to initialize usb_hid!")
                            be.api.setvar("return", "1")
                    else:
                        be.based.error(
                            4,
                            f=vr("opts")["w"][0],
                            prefix=f"{colors.blue_t}ducky{colors.endc}",
                        )
            else:
                be.based.error(2, prefix=f"{colors.blue_t}ducky{colors.endc}")
        else:
            term.write(
                "usb_hid is not enabled in `&/settings.toml`!\n"
                + "To enable it, set `usb_hid_enabled` to 'true' and reboot."
            )
            be.api.setvar("return", "1")
    else:
        term.write("This board does not support usb_hid!")

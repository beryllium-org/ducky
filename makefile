SHELL = bash
all:
	@echo -e "Ljinux ducky.\n\nUsage:\n\tmake package\n\tmake clean"
update_modules:
	@echo "Updating git submodules from remotes.."
	@git submodule update --init --recursive --remote .
	@echo -e "Submodules ready\n\nMake sure to git commit before procceding to make!!"
modules:
	@echo "Preparing git submodules.."
	@git submodule update --init --recursive .
	@echo "Submodules ready"
package: modules
	@python3 -u scripts/make_hid.py
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "ducky.jpk" ]; then rm ducky.jpk; fi
	@if [ -e "./files/__init__.mpy" ]; then rm ./files/__init__.mpy; fi
	@if [ -e "./files/consumer_control_code.mpy" ]; then rm ./files/consumer_control_code.mpy; fi
	@if [ -e "./files/consumer_control.mpy" ]; then rm ./files/consumer_control.mpy; fi
	@if [ -e "./files/keyboard_layout_base.mpy" ]; then rm ./files/keyboard_layout_base.mpy; fi
	@if [ -e "./files/keyboard_layout_us.mpy" ]; then rm ./files/keyboard_layout_us.mpy; fi
	@if [ -e "./files/keyboard.mpy" ]; then rm ./files/keyboard.mpy; fi
	@if [ -e "./files/keycode.mpy" ]; then rm ./files/keycode.mpy; fi
	@if [ -e "./files/mouse.mpy" ]; then rm ./files/mouse.mpy; fi

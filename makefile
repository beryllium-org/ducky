SHELL = bash
all:
	@echo -e "Ljinux ducky.\n\nUsage:\n\tmake package\n\tmake clean"
package:
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "ducky.jpk" ]; then rm package.jpk; fi

#!/usr/bin/env python3
import sys

print("vs_cmds = {")
for ln in sys.stdin:
	ln=ln.strip()
	if not ln:
		continue
	const, nr = ln.split("=")
	nr=int(nr)
	const=const.strip()
	print("\t[%d] = \"%s\"," % (nr, const))
print("}")

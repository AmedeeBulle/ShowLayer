#Name: ShowLayer 42.2
#Info: Show current layer
#Help: ShowLayer
#Depend: GCode
#Type: postprocess

## Written by Amedee
## This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms

# Uses -
# M117 <message> - Set staus message

#history / changelog:
#v42.1: initial release

version = '41.2'
count = '-'

import re

# Read all code...
with open(filename, "r") as f:
	lines = f.readlines()

# ... and write it back!
with open(filename, "w") as f:
	for line in lines:
		f.write(line)
		if line.startswith(';Layer count:'):
			count = line[14:].rstrip()
		if line.startswith(';LAYER:'):
			# New layer -- issue message
			layer = int(line[7:].rstrip()) + 1
			f.write("M117 Layer %d/%s...\n" % (layer, count))

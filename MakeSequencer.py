#!/usr/bin/env python
import re
import os
import itertools
import numpy

original = "/home/ccs/projects/sequencer-files/25raft/FP_ITL_2s_ir2_v25.seq"

with open(original) as f:
	lines = f.readlines()

Val1 = 60+numpy.arange(10)*30
Val2 = 325+numpy.arange(10)*15
for val1, val2 in (list(itertools.product(Val1,Val2))):
	patterns = [
		( r"(ISO1:[\t\s]*).*(ns.*)", val1),
		( r"(ISO2:[\t\s]*).*(ns.*)", val2)
	]

	for i, aline in enumerate(lines):
		for apattern, val in patterns:
			lines[i] = re.sub(apattern, lambda x: "{}{}{}".format(x.group(1), val, x.group(2)), lines[i] )

	with open("out/{}".format(os.path.basename(original).replace(".seq","_{:03d}_{:03d}.seq".format(val1,val2))),"w") as f:
		for aline in lines:
			f.write(aline)




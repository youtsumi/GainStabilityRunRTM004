#!/usr/bin/env ccs-scrtpt
from org.lsst.ccs.scripting import CCS
from ccs import proxies
import java
import jarray
import glob
import os
import time

def commandTarget( self, target ):
        ccstarget = self
        for sub in target.split("/"):
                ccstarget = getattr(ccstarget,sub)()
        return ccstarget

setattr(proxies.ccsProxy, "commandTarget", commandTarget )

def changeSeq( self, seqfile ):
	print("Changing sequencer file to be {}".format(seqfile))
	self.commandTarget("sequencerConfig").change(java.lang.String("sequencer"),java.lang.String(seqfile))

setattr(proxies.ccsProxy, "changeSeq", changeSeq)

fp = CCS.attachProxy("ts8-fp")

try:
	seqfiles = glob.glob("/home/ccs/projects/sequencer-files/timingstudy/*.seq")
	for aseq in seqfiles:
		fp.changeSeq("[E2V:FP_E2V_2s_ir2_v25.seq,ITL:{}]".format(os.path.basename(aseq)))
		time.sleep(15)
		os.system("ccs-script /home/ccs/bot-data.py /home/ccs/projects/fp-scripts-current/examples_ts8/bias.cfg")

finally:
	fp.changeSeq("[E2V:FP_E2V_2s_ir2_v25.seq,ITL:FP_ITL_2s_ir2_v25.seq]")

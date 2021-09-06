from pylsl import StreamInfo, StreamOutlet, local_clock
from RTBox import RTBox
from time import sleep
from random import random

N_TRIALS = 100 # number of events for test

# create lsl outlet
info = StreamInfo('MarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

# initialize RTBox using LSL's local clock
box = RTBox(host_clock = local_clock)
box.clockRatio() # measure and apply clock offset


for i in range(N_TRIALS):

	# send a TTL pulse, get send time
	stamp, _ = box.TTL(0b11111111)

	# send an LSL marker to record timestamp
	outlet.push_sample(['event'], stamp)

	# wait until next event
	sleep(3*random())
# LabStreamingLayer Timing Test

This is a script to help measure the [constant delay](https://sccn.ucsd.edu/~mgrivich/LSL_Validation.html) of your recording hardware when recording over LSL. It requires an [RTBox](https://github.com/xiangruili/RTBox_py) to send TTL pulses and, importantly, to yield accurate timestamps for when those TTLs were actually delivered relative to LSL's local clock.

This should work reasonably well for any device that has an LSL pulgin that (1) uses LSL's `local_clock()` to record timestamps and (2) records the time of retrieved TTL triggers. (Not all LSL plugins will record TTL triggers; for example, the plugin for [EGI' amp server](https://github.com/labstreaminglayer/App-EGIAmpServer) doesn't, but the one for [Brain Products' actiCHamp](https://github.com/brain-products/LSL-actiCHamp) does.)

Just start recording an LSL stream from your hardware's plugin, then run this script which will start a seperate marker stream. Record both streams with [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder). Then you just have to load the resulting XDF file and compute the offset (and jitter) between the hardware events and the software markers.
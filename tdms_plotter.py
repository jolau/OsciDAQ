import matplotlib.pyplot as plt
import numpy as np
from nptdms import TdmsFile
from pathlib import Path
import sys

if len(sys.argv) <= 1:
    sys.exit("No tdms file as command line argument was given.")

tdmsFilePath = Path(sys.argv[1])

if not tdmsFilePath.exists():
    sys.exit("No file does not exist.")

if tdmsFilePath.suffix != ".tdms":
    sys.exit("File is not a TDMS file.")

tdmsFile = TdmsFile.read(tdmsFilePath)
data = tdmsFile["data"]

time = data['Time (s)']
channel1 = data['Channel 1 (V)']
channel2 = data['Channel 2 (V)']

plt.plot(time, channel1)
plt.plot(time, channel2)
plt.show()
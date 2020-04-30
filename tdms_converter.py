import matplotlib.pyplot as plt
import numpy as np
from nptdms import TdmsFile
from pathlib import Path
import sys

# dirPath = Path("/Volumes/GoogleDrive/My Drive/WingtraDrive/technical/Hardware/Projects 2020/20200210 DAQ Payload/OsciDAQ/tdms/")

if len(sys.argv) <= 1:
    sys.exit("No directory as command line argument was given.")

dirPath = Path(sys.argv[1])

tdmsFilePaths = list(dirPath.glob("*.tdms"))
csvDirPath = dirPath.joinpath("csv")
csvDirPath.mkdir(exist_ok=True)

for tdmsFilePath in tdmsFilePaths:
    tdmsFile = TdmsFile.read(tdmsFilePath)
    data = tdmsFile["data"]

    time = data['Time (s)']
    channel1 = data['Channel 1 (V)']
    channel2 = data['Channel 2 (V)']

    stacked = np.column_stack((time, channel1, channel2))

    csvFilePath = csvDirPath.joinpath(tdmsFilePath.stem + ".csv")
    np.savetxt(csvFilePath, stacked, delimiter=",", header=(time.name + "," + channel1.name + "," + channel2.name),
               comments="")
    print("Converted file: " + str(csvFilePath))

print("Converted all files.")

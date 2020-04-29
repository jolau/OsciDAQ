import matplotlib.pyplot as plt
import numpy as np
from nptdms import TdmsFile
from pathlib import Path

# dirPath = Path("/Volumes/GoogleDrive/My Drive/WingtraDrive/technical/Hardware/Projects 2020/20200210 DAQ Payload/OsciDAQ/tdms/")
dirPath = Path("/Users/jolau/Desktop/scope/tdms")

tdmsFilePaths = list(dirPath.glob("*.tdms"))

csvDirPath = dirPath.joinpath("csv")
csvDirPath.mkdir(exist_ok=True)

for tdmsFilePath in tdmsFilePaths:
        tdmsFile = TdmsFile.read(str(tdmsFilePath))
        data = tdmsFile["data"]

        time = data['Time (s)']
        channel1 = data['Channel 1 (V)']
        channel2 = data['Channel 2 (V)']

        stacked = np.column_stack((time, channel1, channel2))

        csvFilePath = csvDirPath.joinpath(tdmsFilePath.stem + ".csv")
        np.savetxt(csvFilePath, stacked, delimiter=",", header=(time.channel + "," + channel1.channel + "," + channel2.channel), comments="")
        print("saved file: " + str(csvFilePath))

print("Converted all files.")



# plt.plot(time, channel1)
# plt.show()

# all_groups = tdms_file.groups()
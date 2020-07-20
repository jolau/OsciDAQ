__author__ = "Jonas Lauener"
__copyright__ = "2020, Jonas Lauener & Wingtra AG"
__licence__ = "Mozilla Public License, v. 2.0, https://mozilla.org/MPL/2.0/"

import argparse

import matplotlib.pyplot as plt
from nptdms import TdmsFile
from pathlib import Path


def main(tdms_file_path):
    tdms_file = TdmsFile.read(tdms_file_path)
    data = tdms_file["data"]

    time = data['Time (s)']
    channel1 = data['Channel 1 (V)']
    channel2 = data['Channel 2 (V)']

    plt.plot(time, channel1)
    plt.plot(time, channel2)
    plt.show()


def existing_tdms_file_path(string):
    path = Path(string)
    if path.exists() and path.suffix == ".tdms":
        return path
    else:
        raise FileNotFoundError(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot TDMS file.')
    parser.add_argument("tdms_file", help="Path to TDMS file.", type=existing_tdms_file_path)

    args = parser.parse_args()
    main(args.tdms_file)
import argparse

import numpy as np
from nptdms import TdmsFile
from pathlib import Path


def main(tdms_dir_path, csv_dir_path):
    tdms_file_paths = list(tdms_dir_path.glob("*.tdms"))
    if csv_dir_path is None:
        csv_dir_path = tdms_dir_path.parent.joinpath(tdms_dir_path.name + "_csv")
        csv_dir_path.mkdir(exist_ok=True)

    for index, tdms_file_path in enumerate(tdms_file_paths):
        tdms_file = TdmsFile.read(tdms_file_path)
        data = tdms_file["data"]

        time = data['Time (s)']
        channel1 = data['Channel 1 (V)']
        channel2 = data['Channel 2 (V)']

        stacked = np.column_stack((time, channel1, channel2))

        csv_file_path = csv_dir_path.joinpath(tdms_file_path.stem + ".csv")
        np.savetxt(csv_file_path, stacked, delimiter=",",
                   header=(time.name + "," + channel1.name + "," + channel2.name),
                   comments="")
        print("Converted file {:d}/{:d}: {}".format(index + 1, len(tdms_file_paths), csv_file_path))

    print("Converted all files.")


def existing_dir_path(string):
    path = Path(string)
    if path.is_dir():
        return path
    else:
        raise NotADirectoryError(string)


def target_dir_path(string):
    path = Path(string)
    path.mkdir(exist_ok=True)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert TDMS files from Waveforms software to CSV.')
    parser.add_argument("tdms_dir", help="Path to directory containing TDMS files.", type=existing_dir_path)
    parser.add_argument("--target_dir", type=target_dir_path,
                        help="Target directory for csv files. Default: 'csv' directory within tdms directory.")

    args = parser.parse_args()
    main(args.tdms_dir, args.target_dir)

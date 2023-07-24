import datetime
import pathlib
from typing import Callable

import pandas as pd


def get_data_from_xlsx(file_path: pathlib.Path) -> list[int]:
    """
    Get the first 500 points from the excel file.

    Args:
        file_path (pathlib.Path): The path to the excel file.

    Returns:
        list[int]: The first 500 points from the excel file.
    """
    return list(pd.read_excel(file_path)["distance(m)"][:500])


def get_data_from_txt(file_path: pathlib.Path) -> tuple[list]:
    """
    Extract the respective time, distance, and signal strengths recorded from
    a text file.

    Args:
        file_path (pathlib.Path): File path to the data.

    Returns:
        tuple[list]: Returns times, distances, and singal_strengths.
    """
    timing = []
    distances = []
    signal_strengths = []

    with open(file_path) as file:
        for measurement in file.readlines():
            t, distance, signal = measurement.split(" ")

            timing.append(datetime.datetime.strptime(t, "%H:%M:%S"))
            distances.append(int(distance))
            signal_strengths.append(int(signal))

    return timing, distances, signal_strengths


def get_data_from_folder(folder_path: pathlib.Path, get_data: Callable) -> list[list[int]]:
    """
    Extract data from each data file in the folder using a specified method.

    Args:
        folder_path (pathlib.Path): The path to the folder.
        get_data (Callable): The function to use to extract data from the files.

    Returns:
        list[list[int]]: Return an array containing a list for each of the first 500
                         points from each excel file in the folder.
    """
    data = []
    for file_path in folder_path.iterdir():
        data.append(get_data(file_path))
    return data

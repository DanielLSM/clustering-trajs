import numpy as np
import pickle5 as pkl
from datetime import datetime

DATA_DIR = "../data/raw/"
PROCESSED_DIR = "../data/processed"


def save_pickle(obj, directory, name):
    with open(directory + name + ".pkl", 'wb') as handle:
        pkl.dump(obj, handle, protocol=pkl.HIGHEST_PROTOCOL)


def load_pickle(directory, name):
    with open(directory + name + ".pkl", 'rb') as handle:
        return pkl.load(handle)


def return_date():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    return dt_string


if __name__ == '__main__':
    file_name = "trajectories_nocollision"
    data = load_pickle(DATA_DIR, file_name)
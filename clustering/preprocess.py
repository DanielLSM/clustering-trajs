from tools import DATA_DIR, PROCESSED_DIR
from tools import load_pickle, save_pickle, return_date


def process_trajectories(file_name, data_dir):
    data = load_pickle(DATA_DIR, file_name)
    import ipdb
    ipdb.set_trace()


if __name__ == '__main__':
    file_name = "trajectories_nocollision"
    process_trajectories(file_name=file_name, data_dir=DATA_DIR)

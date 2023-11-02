import os, pickle


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    return None


def save_data(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

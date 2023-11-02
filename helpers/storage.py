import os, pickle

from base.notes import Notes
from email_address import AddressBook


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    return {'contacts': AddressBook(), 'notes': Notes()}  

def save_data(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
import json
import pickle


class FileHandler:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_pickle(file_path, data):
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
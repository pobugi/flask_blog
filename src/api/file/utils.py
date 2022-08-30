import os

from flask import current_app


class FileUtils:
    @staticmethod
    def create_folder(name):
        path_root = current_app.config["ROOT_FILE_FOLDER"]

        path = os.path.join(path_root, name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

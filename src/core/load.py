import os


def load_into_database(paths: list, parent_path: str):
    for root, dirs, files in os.walk(parent_path):
        for file_name in files:
            paths.append(os.path.join(root, file_name))


def print_list(my_list: list):
    for item in my_list:
        print(item)

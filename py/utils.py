import os

CATEGORYNAMESPACE = 'WO-Nodes'

def get_category(sub_dir = None):
    if sub_dir is None:
        return CATEGORYNAMESPACE
    else:
        return f"{CATEGORYNAMESPACE}/{sub_dir}"


def get_unique_folders(file_list):
    folder_list = set()
    for file_path in file_list:
        folder_path = os.path.dirname(file_path)
        folder_list.add(folder_path)
    folder_list = list(folder_list)
    folder_list.sort()
    if "" in folder_list:
        folder_list[folder_list.index("")] = "[root dir]"
    return folder_list


def filter_file_list_by_dirs_list(file_list, dirs_list):
    if not dirs_list:
        return file_list
    if "[root dir]" in dirs_list:
        dirs_list[dirs_list.index("[root dir]")] = ""
    return [file for file in file_list if any(os.path.dirname(file) == dir for dir in dirs_list)]

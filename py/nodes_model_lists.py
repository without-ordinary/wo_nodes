import folder_paths
from comfy.comfy_types.node_typing import IO
from .utils import get_category, get_unique_folders, filter_file_list_by_dirs_list


###########################
#     Model List Nodes    #
###########################
# Recreated from memory since Manager nuked the first version

class ListCheckpoints:
    CLASSNAME = "WO_ListCheckpointsV1"
    NAME = "List Checkpoints"
    CATEGORY = get_category()

    @classmethod
    def INPUT_TYPES(cls):
        folder_list = get_unique_folders(folder_paths.get_filename_list("checkpoints"))
        return {
            "required": {
                "dirs": (IO.COMBO, { # multi_select causes using new (possible broken) combobox control
                    "default": folder_list[0],
                    "options": folder_list,
                    "multi_select": {"placeholder": "[All Checkpoints]"},
                }),
            },
        }

    OUTPUTS = {"checkpoints": IO.STRING}
    RETURN_TYPES = tuple(OUTPUTS.values())
    RETURN_NAMES = tuple(OUTPUTS.keys())
    FUNCTION = "out"

    def out(self, dirs,):
        checkpoints_list = folder_paths.get_filename_list("checkpoints")
        checkpoints_list = filter_file_list_by_dirs_list(checkpoints_list, dirs)
        return ("\n".join(checkpoints_list),dirs)


#########################
#     Register Nodes    #
#########################
# I'm lazy and don't want to define a bunch of duplicate data in separate file to register nodes.

def get_nodes():
    return [
        ListCheckpoints,
    ]


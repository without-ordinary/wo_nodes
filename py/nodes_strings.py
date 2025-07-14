from comfy.comfy_types.node_typing import IO
from .utils import get_category, remove_trailing_empty_strings

SUB_CATEGORY = "Strings"

#######################
#     String Nodes    #
#######################
# Collection of utility nodes for working with strings

# There are a lot of string literal nodes out there already. This is yet another one.
class StringMultiline:
    CLASSNAME = "WO_StringMultilineV1"
    NAME = "Multiline String"
    CATEGORY = get_category(SUB_CATEGORY)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": (IO.STRING, {"multiline": True, "default": ""}),
            },
        }

    OUTPUTS = {"string": IO.STRING}
    RETURN_TYPES = tuple(OUTPUTS.values())
    RETURN_NAMES = tuple(OUTPUTS.keys())
    FUNCTION = "out"

    def out(self, string,):
        return (str(string),)


class StringJoin:
    CLASSNAME = "WO_StringJoinV1"
    NAME = "Join Strings"
    CATEGORY = get_category(SUB_CATEGORY)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_1": (IO.STRING, {"multiline": False, "default": ""}),
                "string_2": (IO.STRING, {"multiline": False, "default": ""}),
                "string_3": (IO.STRING, {"multiline": False, "default": ""}),
                "string_4": (IO.STRING, {"multiline": False, "default": ""}),
                "string_5": (IO.STRING, {"multiline": False, "default": ""}),
                "separator": (IO.STRING, {
                    "multiline": False, "default": "\\n",
                    "tooltip": "Seperator between strings. If enabled, supports escape characters like: \\t and \\n"
                }),
                "strip": (IO.BOOLEAN , {
                    "default": True,
                    "tooltip": "Remove leading and trailing whitespace, and empty imputs."
                }),
                "sep_escaped": (IO.BOOLEAN, {
                    "default": True,
                    "tooltip": "Enables support for escape characters in seperator field."
                }),
            }
        }

    OUTPUTS = {"string": IO.STRING}
    RETURN_TYPES = tuple(OUTPUTS.values())
    RETURN_NAMES = tuple(OUTPUTS.keys())
    FUNCTION = "out"

    def out(self, string_1, string_2, string_3, string_4, string_5, separator, strip, sep_escaped):
        texts = [string_1, string_2, string_3, string_4, string_5]
        if strip:
            texts = [text.strip() for text in texts if text.strip()]
        else:
            texts = remove_trailing_empty_strings(texts)
        if sep_escaped:
            separator = separator.encode('ascii', 'ignore').decode('unicode_escape')
        return (separator.join(texts),)


#########################
#     Register Nodes    #
#########################
# I'm lazy and don't want to define a bunch of duplicate data in separate file to register nodes.

def get_nodes():
    return [
        StringMultiline,
        StringJoin,
    ]


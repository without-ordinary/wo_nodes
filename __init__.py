"""Top-level package for wo_nodes."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """Without Ordinary"""
__email__ = "without-ordinary@users.noreply.github.com"
__version__ = "0.0.1"

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
def add_nodes(node_classes):
    for node_class in node_classes:
        NODE_CLASS_MAPPINGS[node_class.CLASSNAME] = node_class
        NODE_DISPLAY_NAME_MAPPINGS[node_class.CLASSNAME] = node_class.NAME

from .py.nodes_model_lists import get_nodes as get_model_lists

add_nodes(get_model_lists())


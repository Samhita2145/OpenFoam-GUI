import yaml
from .node import Node

def build_tree_from_dict(data):
    """
    Recursively builds a binary tree from a dictionary
    """
    if data is None:
        return None

    node = Node(data.get("value"))

    node.left = build_tree_from_dict(data.get("left"))
    node.right = build_tree_from_dict(data.get("right"))

    return node


def build_tree_from_yaml(filepath):
    """
    Builds a binary tree from a YAML file
    """
    try:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)

        return build_tree_from_dict(data)

    except FileNotFoundError:
        print("YAML file not found")
        return None
    except yaml.YAMLError:
        print("Error parsing YAML file")
        return None
def build_dict_from_tree(node):
    """
    Recursively builds a dictionary from a binary tree
    """
    if node is None:
        return None

    data = {"value": node.value}

    if node.left is not None:
        data["left"] = build_dict_from_tree(node.left)

    if node.right is not None:
        data["right"] = build_dict_from_tree(node.right)

    return data


def write_tree_to_yaml(root, filepath):
    """
    Writes a binary tree to a YAML file
    """
    try:
        data = build_dict_from_tree(root)

        with open(filepath, "w") as file:
            yaml.dump(data, file, sort_keys=False)

        print(f"Tree successfully written to {filepath}")

    except Exception as e:
        print(f"Error writing YAML file: {e}")

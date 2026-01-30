from .node import Node

def print_tree(node, level=0, prefix="Root:"):
    """Recursively prints the binary tree structure"""
    if node is None:
        return

    indent = " " * (level * 4)
    print(f"{indent}{prefix}{node.value}")

    print_tree(node.left, level + 1, "L---")
    print_tree(node.right, level + 1, "R---")

def add_node_by_path(root, path, value):
    """Adds a node to the binary tree using a path string (L/R)"""
    current = root

    for direction in path[:-1]:
        if direction == "L":
            if current.left is None:
                current.left = Node(None)
            current = current.left
        elif direction == "R":
            if current.right is None:
                current.right = Node(None)
            current = current.right
        else:
            raise ValueError("Path must contain only 'L' or 'R'")

    if path[-1] == "L":
        current.left = Node(value)
    elif path[-1] == "R":
        current.right = Node(value)
    else:
        raise ValueError("Path must contain only 'L' or 'R'")

def edit_node_by_path(root, path, new_value):
    """Edits the value of a node specified by path"""
    current = root

    for direction in path:
        if current is None:
            raise ValueError("Invalid path")

        if direction == "L":
            current = current.left
        elif direction == "R":
            current = current.right
        else:
            raise ValueError("Path must contain only 'L' or 'R'")

    if current is None:
        raise ValueError("Invalid path")

    current.value = new_value
def delete_node_by_path(root, path):
    """Deletes a node from the binary tree using a path"""
    if not path:
        return None  # deleting entire tree

    current = root

    for direction in path[:-1]:
        if current is None:
            raise ValueError("Invalid path")

        if direction == "L":
            current = current.left
        elif direction == "R":
            current = current.right
        else:
            raise ValueError("Path must contain only 'L' or 'R'")

    if path[-1] == "L":
        current.left = None
    elif path[-1] == "R":
        current.right = None
    else:
        raise ValueError("Path must contain only 'L' or 'R'")

    return root


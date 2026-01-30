from binary_tree.node import Node
from binary_tree.tree_utils import (
    add_node_by_path,
    edit_node_by_path,
    delete_node_by_path
)
from binary_tree.yaml_utils import build_tree_from_dict


def test_add_node_by_path():
    root = Node(10)
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)

    assert root.left.value == 5
    assert root.right.value == 15


def test_edit_node_by_path():
    root = Node(10)
    add_node_by_path(root, "L", 5)
    edit_node_by_path(root, "L", 8)

    assert root.left.value == 8


def test_delete_node_by_path():
    root = Node(10)
    add_node_by_path(root, "L", 5)
    delete_node_by_path(root, "L")

    assert root.left is None


def test_build_tree_from_dict():
    data = {
        "value": 1,
        "left": {"value": 2},
        "right": {"value": 3}
    }

    root = build_tree_from_dict(data)

    assert root.value == 1
    assert root.left.value == 2
    assert root.right.value == 3

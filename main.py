from binary_tree.yaml_utils import (
    build_tree_from_yaml,
    write_tree_to_yaml
)
from binary_tree.tree_utils import print_tree

if __name__ == "__main__":
    root = build_tree_from_yaml("./test.yaml")

    print("Tree loaded from YAML:")
    print_tree(root)

    write_tree_to_yaml(root, "output.yaml")

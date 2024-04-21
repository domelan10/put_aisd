from node import Node
from rotate import rotate_left, rotate_right

def height_right(root: Node) -> int:
    if root.right is None:
        return 0
    else:
        return height_right(root.right) + 1

def height_left(root: Node) -> int:
    if root.left is None:
        return 0
    else:
        return height_left(root.left) + 1

def balance(root: Node) -> Node:
    root = shift_right(root)
    
    while height_left(root) < height_right(root):
        root = shift_left(root)
    return root


def shift_right(root: Node) -> Node:
    if root is not None:
        while root.left is not None:
            root = rotate_right(root)
        root.right = shift_right(root.right)
        return root

def shift_left(root: Node) -> Node:
    rotations = height_right(root) // 2
    if rotations == 0:
        return root
    elif rotations == 1:
        return rotate_left(root)
    else:
        root = rotate_left(root)
        root.right = shift_left(root.right)
        return root

if __name__ == '__main__':
    from bst_tree import create_bst_tree
    from show import pre_order
    root, _ = create_bst_tree([9, 5, 7, 15, 10, 18, 19])
    pre_order(root)
    print("\n")
    root = balance(root)
    pre_order(root)
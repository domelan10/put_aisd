from node import Node
from array_create import create_array

def create_avl_tree(array: list, height_right = 0, height_left = 0) -> (tuple[Node, int] | None):
    """
    Create an AVL tree.
    """
    if len(array) == 0:
        return None, max(height_right-1, height_left-1)
    
    m = len(array) // 2

    root = Node(array[m])
    root.left, hl = create_avl_tree(array[:m], height_right, height_left + 1)
    root.right, hr = create_avl_tree(array[m + 1:], height_right + 1, height_left)

    return root, max(hl, hr)

if __name__ == '__main__':
    root, height = create_avl_tree(create_array(11))

    print(root.value, "height:", height)

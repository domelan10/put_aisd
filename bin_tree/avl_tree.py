from node import Node

def create_avl_tree(array: list, height_right = 0, heigh_left = 0) -> (tuple[Node, int] | None):
    if len(array) == 0:
        return None
    
    m = len(array) // 2   

    root = Node(array[m])
    root.left = create_avl_tree(array[:m], height_right, heigh_left += 1)
    root.right = create_avl_tree(array[m + 1:], height_right += 1, heigh_left)

    return root, max(heigh_left, height_right)

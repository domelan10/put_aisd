from node import Node

def create_avl_tree(array: list) -> Node | None:
    if len(array) == 0:
        return None
    
    m = len(array) // 2   

    root = Node(array[m])
    root.left = create_avl_tree(array[:m])
    root.right = create_avl_tree(array[m + 1:])

    return root

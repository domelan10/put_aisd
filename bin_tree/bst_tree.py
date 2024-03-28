from node import Node

def create_bst_tree(array: list) -> Node | None:    
    root = Node(array[0])
    array.pop(0)

    if len(array) == 0:
        return None

    if array[0] > root.value:
        root.right = create_bst_tree(array)
    else:
        root.left = create_bst_tree(array)

    return root
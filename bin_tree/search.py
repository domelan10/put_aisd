def search_max(node) -> int:
    """
    Returns the maximum value in the tree.
    """
    if node.right is None:
        return node.value
    else:
        return search_max(node.right)

def search_min(node) -> int:
    """
    Returns the minimum value in the tree.
    """
    if node.left is None:
        return node.value
    else:
        return search_min(node.left)

def search_key(node, key) -> int:
    """
    Returns the path to the key in the tree.
    """
    result = f'{node.value}'
    if key < node.value:
        if node.left != None:
            result += f' > {search_key(node.left, key)}'
        else:
            result += f' > Not found'
    elif key > node.value:
        if node.right != None:
            result += f' > {search_key(node.right, key)}'
        else:
            result += f' > Not found'
    
    return result
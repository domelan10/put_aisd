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
    
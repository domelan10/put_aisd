from node import Node
from search import search_min

def delete_node(root, val) -> Node:
    """
    Deletes given nodes from the tree.
    """
    
    if root is None:
        return root
    
    if val < root.value:
        root.value = delete_node(root.left, val)

    elif val > root.value:
        root.value = delete_node(root.right, val)
    
    else:
        if root.left is None and root.right is None:
            return None
        
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        min_node = search_min(root.right)
        root.value = min_node.value
        root.right = delete_node(root.right, min_node.value)

    return root
    
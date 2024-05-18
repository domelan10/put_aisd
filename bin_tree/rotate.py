from node import Node

def rotate_right(root: Node) -> Node:
    """
    Rotates a BST tree right
    """
    new_root = root.left
    
    new_right = root
    new_right.left = new_root.right
    
    new_root.right = new_right
    
    return new_root

def rotate_left(root: Node) -> Node:
    """
    Rotates a BST tree left
    """
    new_root = root.right
    
    new_left = root
    new_left.right = new_root.left
    
    new_root.left = new_left
    
    return new_root

if __name__ == '__main__':
    from bst_tree import create_bst_tree
    import show
    
    root, _ = create_bst_tree([9, 5, 7, 15, 10, 18, 19])
    root = rotate_right(root)
    root.right = rotate_right(root.right)
    show.pre_order(root)
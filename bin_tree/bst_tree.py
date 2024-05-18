from node import Node

def create_bst_tree(array: list) -> (tuple[Node, int] | None):
    """
    Create a BST tree from an array.
    """
    if len(array) == 0:
        return None

    root = Node(array[0])
    max_height = 0

    for e in array[1:]:
        height = 0
        curr = root
        while True:
            height += 1
            if e < curr.value:
                if curr.left is None:
                    curr.left = Node(e)
                    break
                else:
                    curr = curr.left
            
            else:
                if curr.right is None:
                    curr.right = Node(e)
                    break
                else:
                    curr = curr.right
            max_height = max(max_height, height)

    return root, max_height + 1
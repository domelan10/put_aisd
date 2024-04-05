from node import Node

def create_bst_tree(array: list) -> Node | None:    
    if len(array) == 0:
        return None

    root = Node(array[0])

    for e in array[1:]:
        curr = root
        while True:
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

    return root
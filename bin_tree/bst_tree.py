from node import Node

def create_bst_tree(array: list) -> (tuple[Node, int] | None):    
    if len(array) == 0:
        return None

    root = Node(array[0])
    height_left = 0
    heiht_right = 0

    for e in array[1:]:
        curr = root
        while True:
            if e < curr.value:
                if curr.left is None:
                    curr.left = Node(e)
                    height_left += 1
                    break
                else:
                    curr = curr.left
            
            else:
                if curr.right is None:
                    curr.right = Node(e)
                    heiht_right += 1
                    break
                else:
                    curr = curr.right

    return root, max(heiht_right, height_left)
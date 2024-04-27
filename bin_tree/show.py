from node import Node

def in_order(node: Node) -> None:
    """
    Prints tree in order (left, current, right).
    """
    # print("Children of node:\n right:", node.right, "\n left:", node.left,"\n") for debugging purposes
    
    if node.left is not None:
        in_order(node.left)

    # print(node.value)

    if node.right is not None:
        in_order(node.right)

def pre_order(node: Node) -> None:
    """
    Prints tree in order (current, left, right).
    """
    # print(node.value)
    
    if node.left is not None:
        pre_order(node.left)

    if node.right is not None:
        pre_order(node.right)
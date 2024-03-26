def in_order(node) -> None:

    if node.left is not None:
        in_order(node.left)

    print(node.value)

    if node.right is not None:
        in_order(node.right)
        
def in_order(node) -> None:
    # print("Children of node:\n right:", node.right, "\n left:", node.left,"\n") for debugging purposes

    if node.left is not None:
        in_order(node.left)

    print(node.value)

    if node.right is not None:
        in_order(node.right)
        
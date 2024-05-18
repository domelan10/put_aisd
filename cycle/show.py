def print_graph(graph: list[list[int]]) -> None:
    print("     ", end = "")
    for i in range(len(graph)):
        print(f"{i}. ", end = "")
    for id, subarray in enumerate(graph):
        print("\n", id, end = ". [")
        for element in subarray:
            print(element, end = ", ")
        print("]", end="")
    print("\n")
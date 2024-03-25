class Node:
    def __init__(self, value: int, root = None):
        self.value = value
        self.left = None
        self.right = None
        self.root = root

    def make_child(self, value):
        if value < self.value:
            self.left = Node(value, self)
        elif value > self.value:
            self.right = Node(value, self)
    
        return Node(value, self.value)

    def get_value(self) -> int:
        return self.value
    
    def find_max(self) -> int:
        if self.right is not None:
            return self.right.find_max()
        else:
            return self.value

def main() -> None:
    root = Node(5)
    root.make_child(6)
    root.make_child(7)
    root.make_child(8)
    root.make_child(9)
    root.make_child(10)
    
    print(root.find_max())
    

if __name__ == '__main__':
    main()
from queue import Queue

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def countLeafNodes(root):
    q = Queue()
    q.put(root)
    counter = 0
    while not q.empty():
        node = q.get()
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
        if node.right is None and node.left is None:
            counter += 1
    return counter


def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.right = Node(2)
    root.right.left = Node(2)
    return root

def main():
    root = buildTree()
    result = countLeafNodes(root)
    print(result)

if __name__ == '__main__':
    main()

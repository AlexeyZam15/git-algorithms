class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = list[TreeNode]()

    def add_child(self, child_node):
        if child_node == self:
            raise AttributeError("cant add itself")
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children
                         if child is not child_node]

    def __str__(self):
        return f"{self.value}"

    def print_tree_node(self):
        if self.children:
            children_l = [child for child in self.children]
            print(f"{self.value} children:", *children_l)
            return [child.print_tree_node() for child in self.children]
        return print(f"{self.value} dont have children")


class BinaryTree:
    def __init__(self, nodes: list[TreeNode]):
        if not nodes:
            raise AttributeError("nodes are empty")
        self.root = nodes[len(nodes) // 2]
        self.make_children(nodes)

    def print_tree(self):
        self.root.print_tree_node()

    def make_children(self, nodes: list):
        size = len(nodes)
        if size == 1:
            return

        half = size // 2
        root = nodes[half]
        root.add_child(nodes[half // 2])
        if size > 2:
            if len(nodes[half + 1:]) == 1:
                root.add_child(nodes[half + 1:][0])
            else:
                root.add_child(nodes[half + 1:][len(nodes[half + 1:]) // 2])
            if size > 3:
                self.make_children(nodes[:half])
                self.make_children(nodes[half + 1:])

    def __find_deep(self, node: TreeNode, value):
        if node.value == value:
            return node
        else:
            for child in node.children:
                result = self.__find_deep(child, value)
                if result:
                    return result
        return None

    def __contains__(self, value):
        if not self.root:
            return False
        node = self.__find_deep(self.root, value)
        if node:
            return True
        return False

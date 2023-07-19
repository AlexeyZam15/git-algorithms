class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, nodes=None):
        if nodes:
            if not getattr(nodes, "pop", None):
                raise TypeError("argument must have attribute 'pop'")
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        if not isinstance(node, Node):
            return self.add_first(Node(node))
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_value, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.value == target_node_value:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_value} not found")

    def add_before(self, target_node_value, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.value == target_node_value:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.value == target_node_value:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_value} not found")

    def add_by_index(self, new_node: Node, index: int):
        if index == 0:
            return self.add_first(new_node)
        node = self.head
        for i in range(index - 1):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count

    def __getitem__(self, item):
        if item > len(self):
            raise IndexError("list index out of range")
        node = self.head
        for i in range(item):
            node = node.next
        return node

    def remove_by_index(self, index):
        if not self:
            raise IndexError("remove from empty list")
        if not index in range(len(self)):
            raise IndexError("list index out of range")
        node = self.head
        if index == 0:
            self.head = node.next
            return
        for i in range(index - 1):
            node = node.next
        node.next = node.next.next

    def get_node(self, value):
        for node in self:
            if node.value == value:
                return node
        return None

    def __setitem__(self, index, value):
        self[index].value = value

    def __contains__(self, value):
        for node in self:
            if node.value == value:
                return True
        return False

    def get_node_index(self, value):
        if not self.__contains__(value):
            return None
        count = 0
        for node in self:
            if node.value == value:
                return count
            count += 1

    def remove(self, value):
        if not self:
            raise IndexError("remove from empty list")

        if self.get_node_index(value) == 0:
            if len(self) == 1:
                self.head = None
                return
            self.head = self.head.next

        prev_node = self.head
        for node in self:
            if node.value == value:
                prev_node.next = node.next
            prev_node = node

    def reverse(self):
        prev = None
        node = self.head
        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        self.head = prev





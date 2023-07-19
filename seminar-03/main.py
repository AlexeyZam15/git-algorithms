from linkedlist import LinkedList, Node


def main():
    # llist = LinkedList()
    # print(llist)
    #
    # # first_node = Node("a")
    # # llist.head = first_node
    # llist = LinkedList(["a"])
    # print(llist)
    #
    # # second_node = Node("b")
    # # third_node = Node("c")
    # # first_node.next = second_node
    # # second_node.next = third_node
    # llist = LinkedList(["a", "b", "c"])
    # print(llist)

    # llist = LinkedList(["a", "b", "c", "d", "e"])
    # print(llist)
    #
    # for node in llist:
    #     print(node)

    # llist = LinkedList()
    # print(llist)
    #
    # llist.add_first(Node("b"))
    # print(llist)
    #
    # llist.add_first(Node("a"))
    # print(llist)

    # llist = LinkedList(["a", "b", "c", "d"])
    # print(llist)
    #
    # llist.add_last(Node("e"))
    # print(llist)
    #
    # llist.add_last(Node("f"))
    # print(llist)

    # llist = LinkedList()
    # llist.add_after("a", Node("b"))

    # llist = LinkedList(["a", "b", "c", "d"])
    # print(llist)
    #
    # llist.add_after("c", Node("cc"))
    # print(llist)
    #
    # llist.add_after("f", Node("g"))

    # llist = LinkedList()
    # llist.add_before("a", Node("a"))

    # llist = LinkedList(["b", "c"])
    # print(llist)
    #
    # llist.add_before("b", Node("a"))
    # print(llist)
    #
    # llist.add_before("b", Node("aa"))
    # llist.add_before("c", Node("bb"))
    # print(llist)
    #
    # llist.add_before("n", Node("m"))

    llist = LinkedList(["1", "2"])
    print(llist)

    llist.add_by_index(Node("0"), 0)
    print(llist)

    llist.add_by_index(Node("11"), 1)
    print(llist)

    llist.add_by_index(Node("4"), 4)
    print(llist)

    print(f'Длина связного списка - {len(llist)}')

    print(llist[4])

    llist.remove_by_index(0)
    print(llist)

    # llist = LinkedList()
    # llist.remove_by_index(0)
    # print(llist)

    llist = LinkedList(["1"])
    print(llist)
    # llist.remove_by_index(1)
    llist.remove_by_index(0)
    print(llist)

    llist.add_first("1")
    print(llist)
    llist[0] = "2"
    print(llist)

    print(llist.get_node_index("2"))
    # print(llist.get_node_index("0"))
    llist.remove("2")
    print(llist)

    llist = LinkedList(["1", "2", "1"])
    print(llist)
    llist.remove("1")
    print(llist)
    llist.remove("2")
    print(llist)
    # llist.remove("2")


if __name__ == '__main__':
    main()

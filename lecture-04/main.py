from trees import TreeNode, BinaryTree


def main():
    nodes = [TreeNode(i) for i in range(0, 13)]

    print(*nodes)

    bin_tree = BinaryTree(nodes)

    bin_tree.print_tree()

    for i in range(13):
        print(i in bin_tree)


if __name__ == "__main__":
    main()

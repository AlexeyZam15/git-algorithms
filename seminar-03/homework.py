from linkedlist import LinkedList


def main():
    llist = LinkedList([i for i in range(10)])
    print(llist)

    llist.reverse()
    print(llist)


if __name__ == "__main__":
    main()

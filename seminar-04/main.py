from hashmap import HashMap


def main():
    hashmap1 = HashMap(4)

    ret = hashmap1.put("1234567891", "Андрей1")
    ret = hashmap1.put("1234567892", "Андрей2")
    ret = hashmap1.put("1234567893", "Андрей3")
    ret = hashmap1.put("1234567894", "Андрей4")
    ret = hashmap1.put("1234567895", "Андрей5")
    ret = hashmap1.put("1234567896", "Андрей6")
    ret = hashmap1.put("1234567897", "Андрей7")
    ret = hashmap1.put("1234567898", "Андрей8")
    ret = hashmap1.put("1234567899", "Андрей9")

    # ret = hashmap1.put("123456789", "Андрей1")
    # hashmap1.print()
    # ret = hashmap1.put("123456788", "Василий")
    # hashmap1.print()
    #
    # print(hashmap1.get("123456788"))
    # ret = hashmap1.put("123456788", "Александр")
    # hashmap1.print()
    # print(hashmap1.get("123456788"))
    #
    # ret = hashmap1.remove("123456789")
    # print(ret)
    # ret = hashmap1.remove("123456789")
    # print(ret)
    #
    # ret = hashmap1.get("123456789")
    # print(ret)

    hashmap1.print()

    return


if __name__ == "__main__":
    main()

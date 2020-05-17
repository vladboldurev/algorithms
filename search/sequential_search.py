def sequential_search(data_list, item):
    pos = 0
    found = False

    while pos < len(data_list) and not found:
        if data_list[pos] == item:
            found = True
        else:
            pos += 1

    return found

def ordered_sequential_search(data_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(data_list) and not found and not stop:
        if data_list[pos] == item:
            found = True
        else:
            if data_list[pos] > item:
                stop = True
            else:
                pos += 1

    return found


if __name__ == "__main__":
    data_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    item = 17
    print(100%11)
    print(sequential_search(data_list, item))

    data_list = [1, 2,  8, 17, 19, 32, 42, 53, 60]
    item = 17
    print(ordered_sequential_search(data_list, item))
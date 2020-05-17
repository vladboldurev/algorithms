def bin_search(items, item):

    found = False
    first = 0
    last = len(items) - 1

    while not found and first <= last:
        midpoint = (first + last)//2
        if items[midpoint] == item:
            found = True
        elif items[midpoint] > item:
            last = midpoint - 1
        elif items[midpoint] < item:
            first = midpoint + 1

    return found


if __name__ == "__main__":
    data_list = [1, 4, 6, 9, 11, 12, 17, 21, 23]
    item = 0
    print(bin_search(data_list, item))
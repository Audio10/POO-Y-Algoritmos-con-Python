import  random


def binary_search(ordered_list, start, end, target):
    """
    :param ordered_list: Already ordered list
    :param start: Search start
    :param end: Search end
    :param target: Target to find
    """
    if start > end:
        return False

    medio = (start + end) // 2

    if ordered_list[medio] == target:
        return True
    elif ordered_list[medio] < target:
        return binary_search(ordered_list, medio + 1, end, target)
    else:
        return binary_search(ordered_list, start, medio - 1, target)


if __name__ == '__main__':
    list_size = int(input('What is the list size'))
    objective = int(input("What is the number that you're search"))
    ordered_list = sorted([random.randint(0, 100) for i in range(list_size)])
    found = binary_search(ordered_list, 0, len(ordered_list), objective)
    print(ordered_list)
    print(f'El elemento {objective} {"esta" if found else "no esta"} en la lista')
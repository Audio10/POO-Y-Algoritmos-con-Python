import random


def sort_by_mix(my_list):
    if len(my_list) > 1:
        medium = len(my_list) // 2
        left = my_list[:medium]
        right = my_list[medium:]
        print(left, '*' * 5, right)

        # recursive call on each half
        sort_by_mix(left)
        sort_by_mix(right)

        # Iterators to traverse the two sublists
        i = 0
        j = 0
        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}')
        print(my_list)
        print('-' * 50)

    return my_list


if __name__ == '__main__':
    list_size = int(input('What is the list size? '))

    my_list = [random.randint(0, 100) for i in range(list_size)]
    print(my_list)
    print('-' * 20)

    ordered_list = sort_by_mix(my_list)
    print(ordered_list)
import random


def linea_search(lista, objetivo):
    """Linear Search have an algorithmic complexity of 0 (n)"""
    match = False  # O(1)

    for element in lista:  # O(n)
        if element == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('What is the list size'))
    objective = int(input("What is the number that you're search"))
    disordered_list = [random.randint(0, 100) for i in range(list_size)]
    found = linea_search(disordered_list, objective)
    print(disordered_list)
    print(f'El elemento {objective} {"esta" if found else "no esta"} en la lista')

def search_index(lst, left, right, element):

    if left > right:
        return "Търсеният елемент не се намира в масива"

    center_index = (left + right) // 2

    if lst[center_index] == element:
        return center_index

    elif lst[center_index] > element:
        return search_index(lst, left, center_index - 1, element)

    else:
        return search_index(lst, center_index + 1, right, element)


numbers = [1, 3, 5, 7, 9, 11, 13]
print(search_index(numbers, 0, len(numbers) - 1, 11))

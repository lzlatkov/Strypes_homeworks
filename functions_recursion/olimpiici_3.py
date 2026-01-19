def search_element(lst, searched_index, left, right):
    if left > right:
        return "not found"

    center = (left + right) // 2
    if lst[center] == searched_index:
        return f"found at {center}"
    elif lst[center] > searched_index:
        return search_element(lst, searched_index, left, center - 1)
    else:
        return search_element(lst, searched_index, center + 1, right)


my_list = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256,
           263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444,
           486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638,
           640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898,
           900, 903, 908, 909, 959, 988]

searched = int(input())

print(search_element(my_list, searched, 0, len(my_list) - 1))

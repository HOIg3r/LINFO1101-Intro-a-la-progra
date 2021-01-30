def maximum_index(lst):
    index = 0
    max_value = 0
    best_index = 0
    if lst == []:
        return None
    else:
        for element in lst:
            if element > max_value:
                best_index = index
                max_value = element
            index += 1
        return best_index
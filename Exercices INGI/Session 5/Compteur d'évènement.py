def count(events, i, j):
    new_tuple = (i,j)
    count = 0
    for element in events:
        if new_tuple == element:
            count += 1
    return count
        
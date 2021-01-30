def collect(filename):
    collected = {}
    with open(filename) as file:
        data = file.readlines()
    pattern = treatment(extract(data))
    collected[pattern] = 1
    return collected
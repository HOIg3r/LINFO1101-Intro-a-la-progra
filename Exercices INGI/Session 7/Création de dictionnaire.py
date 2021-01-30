def create_dict(l):
    d = {}
    for coo in l:
        try:
            d[coo[0]] += [coo[1]]
        except:
            d[coo[0]] = [coo[1]]
    return d
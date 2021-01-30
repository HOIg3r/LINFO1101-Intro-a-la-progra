def get_country(l, name):
    
    for dict in l:
        if dict["City"] == name:
            return dict["Country"]
    return False
        
def __str__(self):
    parse_lst = []
    element = self.first()
    if element is not None:
        parse_lst.append(element.value())
        while element.next() is not None:
            element = element.next()
            parse_lst.append(element.value())
    str_lst = "["
    for i in parse_lst:
        str_lst += " {}".format(i)
    str_lst += " ]"
    return str_lst
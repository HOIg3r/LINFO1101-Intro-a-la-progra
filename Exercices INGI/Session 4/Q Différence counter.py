if lst == []:
    return None
lst_check = []
for element in lst:
    if element not in lst_check:
        lst_check.append(element)

        
return (len(lst_check))
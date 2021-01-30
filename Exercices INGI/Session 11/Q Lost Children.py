try:
    child = first_child
    every_child = child.is_next_valid()
    child = child.next_child()
    while child != first_child or not every_child:
        every_child = child.is_next_valid()
        child = child.next_child()
except:
    return False
return every_child
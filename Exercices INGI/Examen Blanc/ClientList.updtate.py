if self.last == None:
    new_client = Client(name, pin)
    self.last = ClientList.Node(new_client, None)
else:
    current = self.last
    while current is not None:
        if current.data.userName == name:
            node.data.setPin(pin)
            found = True
            break
        current = current.link
    if not found:
        new_client = Client(name, pin)
        self.last = Clientlist.Node(new_client, None)
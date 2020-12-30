import assistant as l

#fonction qui test le programme
def test():
    assert l.file("")
    assert l.file("all-words.dat")
    assert l.file("all-words.txt")
    assert l.info()
    assert l.dictionary()
    assert l.search("e")
    assert l.sum("23 324 23")
    assert l.sum("Efre 34 E")
    assert l.avg("144 324 43 156")
    assert l.exit()
    assert l.help()
test()
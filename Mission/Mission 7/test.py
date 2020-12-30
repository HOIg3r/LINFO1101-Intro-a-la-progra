import search as s

if __name__ == '__main__':
    def test():
        assert s.readfile("text_example_1.txt")
        assert s.readfile("")
        assert s.readfile("text_example_2.txt")
        assert s.get_words("gun fournaise mauvaise, situation !")
        assert s.get_words("")
        assert s.create_index("text_example_1.txt")
        assert s.create_index("text_example_2.txt")
        assert s.create_index("")
        assert s.get_lines("situation","text_example_1.txt")
        assert s.get_lines("wallon","text_example_2.txt")
        assert s.get_lines("","")

test()


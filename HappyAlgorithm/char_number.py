
class CharItem(object):

    def __init__(self, char, leading=False, value=-1):
        self.char = char
        self.leading = leading
        self.value = value


class ExhaustiveProblem(object):

    @classmethod
    def make_integer(cls, string, char_infos):

        integer = 0
        for char in string:
            integer = integer * 10 + char_infos[char].value

        return integer

    @classmethod
    def check_result(cls, char_infos):
        a = cls.make_integer("WWWDOT", char_infos)
        b = cls.make_integer("GOOGLE", char_infos)
        c = cls.make_integer("DOTCOM", char_infos)
        if a - b == c:
            print(f"{a} - {b} = {c}")
            print(char_infos)
        else:
            print(f"{a} {b} {c}")

    def __init__(self, char_items):
        self.char_items = char_items
        self.char_infos = {}
        for char_item in char_items:
            self.char_infos[char_item.char] = char_item
        self.char_num = len(char_items)

    def solve(self, index=0):

        if index == self.char_num:
            self.check_result(self.char_infos)
            return

        used_num = []
        for num in range(0, 10):

            if (num in used_num) or ((num == 0) and self.char_items[index].leading):
                continue

            self.char_items[index].value = num
            used_num.append(num)
            self.solve(index + 1)

            used_num.pop(-1)


def main():
    char_items = [
        CharItem('W', True),
        CharItem('G', True),
        CharItem('D', True),
        CharItem('O', True),
        CharItem('T', True),
        CharItem('L', True),
        CharItem('E', True),
        CharItem('C', True),
        CharItem('M', True),
    ]

    ExhaustiveProblem(char_items).solve()


if __name__ == "__main__":
    main()

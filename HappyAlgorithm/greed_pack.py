class TagObject(object):

    def __init__(self, no, weight, price, status=0):
        self.no = no
        self.weight = weight
        self.price = price
        self.status = status    # 0:未选中  1:已选中 2:不可选

    def __str__(self):
        return f"no: {self.no} weight: {self.weight}  price:{self.price}"


def weight_sorted_func(tags):
    return sorted(tags, key=lambda tag: tag.weight)


def price_sorted_func(tags):
    return sorted(tags, key=lambda tag: tag.price, reverse=True)


def density_sorted_func(tags):
    return sorted(tags, key=lambda tag: tag.price / tag.weight, reverse=True)


POLICY_FUNC_MAP = {
    "weight": weight_sorted_func,
    "price": price_sorted_func,
    "density": density_sorted_func
}


class TagSpaceProblem(object):

    @classmethod
    def policy_func(cls, tags, total, polidy_type):

        tags = [tag for tag in tags if tag.status == 0]

        tags = POLICY_FUNC_MAP[polidy_type](tags)

        for tag in tags:
            if tag.weight > total:
                tag.status = 2
                continue
            elif tag.weight <= total:
                tag.status = 1
                return tag

        return None

    def __init__(self, tags: list, total: int):
        self.tags = tags
        self.total = total

    def greed_algo(self, polidy_type):

        select_tags = []

        while self.total > 0:
            tag = self.policy_func(self.tags, self.total, polidy_type=polidy_type)
            if tag == None:
                break

            self.total -= tag.weight
            select_tags.append(tag)

        self.print_result(select_tags)

    def print_result(self, select_tags):
        total_weight = 0
        total_price = 0
        for select_tag in select_tags:
            total_weight += select_tag.weight
            total_price += select_tag.price
            print(select_tag)

        print(f"weight: {total_weight}   price:{total_price}")


def main():
    tags = [
        TagObject(1, 35, 10),
        TagObject(2, 30, 40),
        TagObject(3, 60, 30),
        TagObject(4, 50, 50),
        TagObject(5, 40, 35),
        TagObject(6, 10, 40),
        TagObject(7, 25, 30),
    ]

    problem = TagSpaceProblem(tags, total=150)
    problem.greed_algo(polidy_type="density")


if __name__ == "__main__":
    main()

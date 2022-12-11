from functools import reduce


class Monkey:
    def __init__(self, info: dict):

        self.items = [int(x) for x in info["Starting items"].split(',')]
        self.operation = eval(
            f"lambda old: {' '.join(info['Operation'].split()[2:])}")

        self.modulo = int(info["Test"].split()[-1])
        self.test = lambda x: x % self.modulo == 0
        self.if_true = int(info["If true"].split()[-1])
        self.if_false = int(info["If false"].split()[-1])
        self.items_inspected = 0

    def inspect(self):
        self.items_inspected += 1
        return self.items[0]

    def throw(self, monkey, item):
        self.items.pop(0)
        monkey.items.append(item)


def setup() -> list:
    with open('input.txt') as file:
        monkeys_raw = file.read().strip().split('\n\n')

    monkeys = []
    for monkey in monkeys_raw:
        data = monkey.split('\n')
        monkey_dict = {}
        for row in data:
            key, content = row.split(':')
            monkey_dict[key.strip()] = content.strip()
        monkeys.append(Monkey(monkey_dict))

    return monkeys


def round(part: int, monkeys: list):
    m = reduce(lambda x, y: x*y, [m.modulo for m in monkeys])
    for monkey in monkeys:
        while monkey.items:
            worry_level = monkey.inspect()
            if part == 2:
                worry_level = worry_level % m

            worry_level = monkey.operation(worry_level)

            if part == 1:
                worry_level = worry_level // 3

            if monkey.test(worry_level):
                monkey.throw(monkeys[monkey.if_true], worry_level)
            else:
                monkey.throw(monkeys[monkey.if_false], worry_level)


def play(part: int, rounds: int):
    monkeys = setup()

    for _ in range(rounds):
        round(part, monkeys)
        print(_)

    top_monkey_business = sorted(
        [monkey.items_inspected for monkey in monkeys], reverse=True)[:2]
    return reduce(lambda x, y: x * y, top_monkey_business)


print("Part 1:", play(1, 20))
print("Part 2:", play(2, 10000))

from functools import cache
import re


class Valve:
    def __init__(self, name: str, rate: int, valves_connected: list[str], num: int):
        self.name = name
        self.rate = rate
        self.valves_connected = valves_connected
        self.open = False
        self.num = num

    def get_neighbors(self):
        return [valves[valve_name] for valve_name in self.valves_connected]


with open('input.txt') as file:
    valves_raw = file.readlines()

valves = {}
for num, valve_raw in enumerate(valves_raw):
    valve_names = re.findall(r'([A-Z][A-Z])+', valve_raw)
    valve_name = valve_names.pop(0)
    valve_rate = int(re.findall(r'\d+', valve_raw)[0])
    valves[valve_name] = Valve(valve_name, valve_rate, valve_names, num)


# Thanks to 0xdf for his solution. It's the only one I (almost) understood.
# Credits: https://gitlab.com/0xdf/aoc2022/-/blob/main/day16/day16.py
@cache
def get_score(valve, time, state, elephant=False):
    if time == 0:
        if elephant:
            # Start over for the elephant
            return get_score(valves['AA'], 26, state)
        return 0

    score = max(get_score(neighbor, time - 1, state, elephant)
                for neighbor in valve.get_neighbors())

    if valve.rate > 0 and not state[valve.num]:
        new_state = list(state)
        new_state[valve.num] = True
        score = max(
            score,
            (time - 1) * valve.rate +
            get_score(valve, time - 1, tuple(new_state), elephant)
        )
    return score


print("Part 1:", get_score(valves['AA'], 30, tuple(
    [valve.open for valve in valves.values()])))

print("Part 2:", get_score(valves['AA'], 26, tuple(
    [valve.open for valve in valves.values()]), True))

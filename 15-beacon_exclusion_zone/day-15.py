from dataclasses import dataclass
from functools import partial
import re
from tqdm import tqdm
from multiprocessing import Pool


def manhattan_distance(x1: int, x2: int, y1: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


@dataclass
class Sensor:
    x: int
    y: int
    radius: int

    def get_limits(self, y):
        delta_y = abs(y - self.y)
        return self.x - (self.radius - delta_y), self.x + (self.radius - delta_y)


sensors = []

with open('input.txt') as file:
    objects_raw = file.readlines()

for line in objects_raw:
    info = re.findall(r'-?\d+', line)

    sensor_x, sensor_y, beacon_x, beacon_y = map(
        lambda x: int(x), info)

    radius = manhattan_distance(sensor_x, beacon_x, sensor_y, beacon_y)

    new_sensor = Sensor(sensor_x, sensor_y, radius)
    sensors.append(new_sensor)

sensors.sort(key=lambda x: x.radius, reverse=True)


def get_no_beacon_spots(y: int):
    covered = set()
    for sensor in sensors:
        x_range_min, x_range_max = sensor.get_limits(y)
        covered.update(set(range(x_range_min, x_range_max + 1)))
    return len(covered) - 1


def point_in_sensor_range(x, y) -> bool:
    for sensor in sensors:
        yield manhattan_distance(sensor.x, x, sensor.y, y) <= sensor.radius


def find_candidates(y: int, sensor):
    x_min, x_max = sensor.get_limits(y)

    for x in [x_min - 1, x_max + 1]:
        if x < 0 or x > LIMIT:
            continue
        if any(point_in_sensor_range(x, y)):
            continue
        return (x, y)


if __name__ == '__main__':
    print("Part 1:", get_no_beacon_spots(y=2000000))

    LIMIT = 4000000
    for sensor in tqdm(sensors):
        y_range = range(max(sensor.y - sensor.radius, 0),
                        min(sensor.y + sensor.radius, LIMIT) + 1)

        with Pool(5) as p:
            a = partial(find_candidates, sensor=sensor)
            candidates = p.map(a, y_range)

        candidates = [c for c in candidates if c]
        if candidates:
            x, y = candidates[0]
            print("Part 2:", (x * LIMIT) + y)
            break

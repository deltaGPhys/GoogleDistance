import json


class MathFunctions:

    @staticmethod
    def calc_pct_diff(num1: int, num2: int) -> float:
        return abs(2*(num2 - num1)/(num1 + num2))

    @staticmethod
    def calc_distance(x1: int, y1: int, x2: int, y2:int) -> float:
        return ((x2-x1)**2 + (y2-y1)**2)**.5

class FileFunctions:

    @staticmethod
    def open_json(file: str) -> json:
        with open(file) as f:
            data = json.load(f)['timelineObjects']
        return data

    @staticmethod
    def print_primary_nodes(json):
        for node in json:
            print(next(iter(node)))

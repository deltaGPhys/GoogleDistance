import json
import os


class MathFunctions:

    @staticmethod
    def calc_pct_diff(num1: int, num2: int) -> float:
        return abs(2*(num2 - num1)/(num1 + num2))

    @staticmethod
    def calc_distance(x1: int, y1: int, x2: int, y2:int) -> float:
        return ((x2-x1)**2 + (y2-y1)**2)**.5

    @staticmethod
    def lat_fix(num: int) -> int:
        if num > 900000000:
            num = num - 4294967296
        return num

    @staticmethod
    def long_fix(num: int) -> int:
        if num > 1800000000:
            num = num - 4294967296
        return num


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

    @staticmethod
    def file_stitcher(folder: str, name: str):
        files = [i for i in os.listdir(folder) if i.endswith("json") and not i == name]

        mega_file = []
        file_num = 0
        for file in files:
            print(file)
            f = open(folder+"/"+file).readlines()
            f = [i.strip('\n') for i in f]
            if file_num != 0:
                f = f[2:]
            if file_num != len(files)-1:
                f = f[:-2]
                f[-1] = f[-1] + ","
            mega_file = mega_file + f
            file_num = file_num + 1

        output_file = open(folder+"/"+name, 'w')

        output_file.write('\n'.join(mega_file))

        output_file.close()

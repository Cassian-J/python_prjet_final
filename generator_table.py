import random

class GeneratorTable:
    @staticmethod
    def generate(col, row, table):
        return [[random.choice(table) for _ in range(col)] for _ in range(row)]
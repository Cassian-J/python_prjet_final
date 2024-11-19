import random


def generate(column,line,table):
    return [[random.choice(table) for _ in range(column)]for _ in range(line)]
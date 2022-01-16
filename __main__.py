#! python3

import matplotlib as plt
import statistics
import numpy
from math import floor, ceil

class NumberSet:
    def __init__(self, numbers: list):
        self.numbers = numbers
        numbers.sort()

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        # statistics.median(self.numbers) could work here, but I have my own implementation:
        if len(self.numbers) % 2 == 1:
            return self.numbers[ceil(len(self.numbers) / 2) - 1]
        else:
            half_index = len(self.numbers) / 2 - 0.5
            return sum([self.numbers[floor(half_index)], self.numbers[ceil(half_index)]]) / 2

if __name__ == '__main__':
    number_set = NumberSet([3,4,5,6,2,1])

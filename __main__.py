#! python3

import matplotlib as plt
import statistics
import numpy
from math import floor, ceil

class NumberSet:
    def __init__(self, numbers: list):
        self.numbers = sorted(numbers)
        self.mean = self.get_mean()
        self.median = self.get_median()
        self.mode = self.get_mode()

    def set_numbers(self, numbers: list):
        self.__init__(numbers)

    def get_state(self):
        return {
                'numbers': self.numbers,
                'mean': self.mean,
                'median': self.median,
                'mode': self.mode
            }

    def get_mean(self):
        '''
        Returns the mean of the data points.
        '''
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        '''
        Returns the median of the data points.
        '''        
        middle_index = len(self.numbers) // 2

        if len(self.numbers) % 2 == 1:
            return self.numbers[middle_index]
        else:
            return sum(self.numbers[middle_index - 1:middle_index + 1]) / 2

    def get_mode(self):
        '''
        Returns a list of most frequently occuring data points.
        '''
        count = {}
        for number in self.numbers:
            if number not in count.keys():
                count[number] = 1
            else:
                count[number] += 1

        max_occurrences = 0
        for number in count.keys():
            if count[number] >= max_occurrences:
                if count[number] > max_occurrences: key = []
                key.append(number)
                max_occurrences = count[number]

        return key

if __name__ == '__main__':
    number_set = NumberSet([3,4,5,6,6,2,1])
    print(number_set.get_state())
    number_set.set_numbers([1,2,3,5,6,7])
    print(number_set.get_state())

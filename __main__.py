#! python3

import numbers
import matplotlib as plt
import statistics
import numpy
from math import floor, ceil

class NumberStatistics:
    def __init__(self, numbers: list):
        self.numbers = sorted(numbers)
        try:
            self.mean = self.get_mean()
            self.median = self.get_median()
            self.mode = self.get_mode()
        except ZeroDivisionError:
            print('Your entry cannot be blank.\n\n')

    def set_numbers(self, numbers: list):
        self.__init__(numbers)

    def get_mean(self, **kwargs):
        '''
        Returns the mean of the data points.
        '''
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = self.numbers
        return sum(data) / len(data)

    def get_median(self, **kwargs):
        '''
        Returns the median of the data points.
        ''' 
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = self.numbers
        
        middle_index = len(data) // 2

        if len(data) % 2 == 1:
            return data[middle_index]
        else:
            return sum(data[middle_index - 1:middle_index + 1]) / 2

    def get_mode(self, **kwargs):
        '''
        Returns a list of most frequently occuring data points.
        '''
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = self.numbers
        
        count = {}
        for number in data:
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
    while True:
        number_list = NumberStatistics([float(x) for x in input('Enter the list items: ').split()])

        if number_list.numbers == []: continue
        for key in number_list.__dict__.keys():
            print(f"{key}:".ljust(10, ' ') + str(number_list.__dict__[key]))
        print('\n')

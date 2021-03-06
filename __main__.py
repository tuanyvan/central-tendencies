#! python3

import matplotlib.pyplot as plt
from math import floor, ceil

class NumberStatistics:
    def __init__(self, items: list):
        self.items = sorted(items)
        try:

            self.mean = self.get_mean()
            self.median = self.get_median()
            self.mode = self.get_mode()
            self.q1 = self.get_median(data=[x for x in self.items if x < self.median])
            self.q2 = self.median
            self.q3 = self.get_median(data=[x for x in self.items if x > self.median])
            self.iqr = self.q3 - self.q1
            self.lower_whisker = self.q1 - 1.5 * self.iqr
            self.upper_whisker = self.q3 + 1.5 * self.iqr

        except ZeroDivisionError:
            print('Your entry cannot be blank.\n\n')
    
    def find_data(self, kwarg_list):
        '''
        Looks for 'data' in kwargs and returns it, otherwise returns self.items
        '''
        if 'data' in kwarg_list:
            return kwarg_list['data']
        else:
            return self.items

    def calculate_statistics(function):
        '''
        Wrapper function to reduce calls to self.find_data().
        '''
        def calculation(self, **kwargs):
            data = self.find_data(kwargs)
            if 'p' in kwargs:
                tendency = function(data, kwargs['p'])
            else:
                tendency = function(data)
            return tendency
        return calculation

    def set_items(self, items: list):
        self.__init__(items)

    @calculate_statistics
    def get_mean(data):
        '''
        Returns the mean of the data points.
        '''
        return sum(data) / len(data)

    @calculate_statistics
    def get_median(data):
        '''
        Returns the median of the data points.
        '''         
        middle_index = len(data) // 2

        if len(data) % 2 == 1:
            return data[middle_index]
        else:
            return (data[middle_index - 1] + data[middle_index]) / 2

    @calculate_statistics
    def get_mode(data):
        '''
        Returns a list of most frequently occuring data points.
        '''

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

    @calculate_statistics
    def get_percentile(data, percentile):
        '''
        Returns the value at which the percentile% of data is below or equal to..
        '''
        rank = (percentile / 100) * (len(data) + 1)
        if rank % 1 == 0:
            if percentile == 100:
                return data[:-1]
            else:
                return data[int(rank) - 1]
        else:

            lower_datum = floor(rank) - 1
            if lower_datum < 0: lower_datum = 0
            
            upper_datum = ceil(rank) - 1
            if upper_datum >= len(data): upper_datum = len(data) - 1

            return (data[lower_datum] + data[upper_datum]) / 2


if __name__ == '__main__':

    while True:

        # Instantiate the Figure and axes.Axes object.
        fig, ax = plt.subplots(figsize=(5,5), constrained_layout=True)

        # Get user number input.
        numbers = NumberStatistics([float(x) for x in input('Enter the list items: ').split()])

        if numbers.items == []: continue
        
        # Print all the properties of the numbers.
        for key in numbers.__dict__.keys():
            print(f"{key}:".ljust(15, ' ') + str(numbers.__dict__[key]))
        print('\n')

        # Create a boxplot using the information of the object.
        ax.boxplot(numbers.items, vert=False, whis=1.5, meanline=True, showmeans=True)
        ax.set_title('Boxplot Given User Data Input')
        
        plt.show()


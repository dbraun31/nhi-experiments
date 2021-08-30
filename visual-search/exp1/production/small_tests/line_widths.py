import sys
import numpy as np

line_width_container = np.linspace(1.2, 4, 10)
#line_width_container = [round(x, 4) for x in line_width_container]


range_to_width = {}

percentages = [.02, .07, .07] + [.17]*4 + [.07, .07, .02]

base_percentage = 0
for percentage, line_width in zip(percentages, line_width_container):
    range_to_width[base_percentage, base_percentage+percentage] = line_width
    base_percentage += percentage +.00001
    
print('\n')
print(range_to_width)


def choose_line_width():
    ## draw random from uniform distribution, choose line width
    random_number  = round(np.random.uniform(), 3)
    for key in range_to_width:
        if random_number >= key[0]  and random_number < key[1]:
            return range_to_width[key]




## initialize full container
line_width_container_original = []

for i in range(400):
    line_width_container_original.append(choose_line_width())
    

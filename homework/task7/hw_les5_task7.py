import os
import json

file_to_read_path = os.path.join(os.path.dirname(__file__), 'firms.txt')
file_to_write_path = os.path.join(os.path.dirname(__file__), 'firms.json')

result = []
profit = {}
average = []

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1


result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)

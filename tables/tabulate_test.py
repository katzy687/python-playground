"""
https://stackoverflow.com/a/40056796
"""

import tabulate

dataset = [
    {'Address': 1, 'Major': 'Biology', 'GPA': '2.4', 'Name': 'Edward'},
    {'Address': 2, 'Major': 'Physics', 'GPA': '2.9', 'Name': 'Emily'},
    {'Address': 3, 'Major': 'Mathematics', 'GPA': '3.5', 'Name': 'Sarah'}
]

header = dataset[0].keys()
rows = [x.values() for x in dataset]
table = tabulate.tabulate(rows, header, tablefmt='grid')
print(table)

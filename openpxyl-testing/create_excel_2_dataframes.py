import openpyxl
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from dataclasses import dataclass

file_name = "test.xlsx"
wb = openpyxl.Workbook()

# rename first sheet
ws = wb.active
ws.title = "my sheet 1"


# convert list of objects to dataframe then write to excel

@dataclass
class Person:
    name: str
    age: int


data = [Person("alice", 26), Person("tim", 27)]
data2 = [Person("brit", 26), Person("hank", 27)]

data_dicts = [x.__dict__ for x in data]
data_dicts2 = [x.__dict__ for x in data2]

df = pd.DataFrame(data_dicts)
df2 = pd.DataFrame(data_dicts2)
df.insert(2, "", "")
joined = pd.concat([df, df2], axis=1)
for r in dataframe_to_rows(joined, index=False, header=True):
    ws.append(r)

wb.save(file_name)

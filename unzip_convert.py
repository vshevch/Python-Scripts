#This script is used by server to unzip uploaded file and convert it to .csv format for further processing by Informatica

import os
import pandas as pd

os.system('cd ~; unzip python_test.zip')

df = pd.read_excel('/home/vs3579515/python_test.xlsx')
df.to_csv('/home/vs3579515/success_test.csv')

print("Success!") # the line is not required

import pandas as pd
from tableone import TableOne, load_dataset

sparcs =pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

##data set 2
example_data=load_dataset('pn2012')

## recode death where 0 is alive and 1 is 
example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
example_data_categorical = ['ICU', 'death']
example_data_groupby = ['death']

example_data_labels={'death': 'mortality'}

exampleTab1 = TableOne(example_data, columns=example_data_columns, categorical=example_data_categorical, groupby=example_data_groupby, rename=example_data_labels, pval=False)
exampleTab1
print(exampleTab1.tabulate(tablefmt = "fancy_grid"))
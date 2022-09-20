import pandas as pd## import pandas for general file types 
from tableone import TableOne, load_dataset



########################
### load in the data 
########################
sparcs =pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

sparcs.columns
sparcs_data = list(sparcs)
sparcs_data
sparcs_data_columns= list ['age_group','length_of_stay', 'ccs_diagnosis_code','ccs_procedure_code', 'apr_drg_code','apr_mdc_code','apr_severity_of_illness_code']
       ##'apr_risk_of_mortality', 'birth_weight', 'abortion_edit_indicator','emergency_department_indicator', 'total_charges', 'total_costs'}] 
sparcs_data_groupby = ['age_group']
sparcs_data_labels={'apr_risk_of_mortality': 'mortality'}
ex_sparces=TableOne(sparcs_data, columns=sparcs_data_columns, groupby=sparcs_data_groupby, rename=sparcs_data_labels, pval=False)
print(ex_sparces.tabulate(tablefmt = "fancy_grid"))
mytable.to_excel('mytable.xlsx')
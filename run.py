import pandas as pd## import pandas for general file types 
from tableone import TableOne, load_dataset

########################
### load in the data ,dataset 1

##import pandas as pd
##from tableone import TableOne, load_dataset



##data set 2
##example_data=load_dataset('pn2012')

## recode death where 0 is alive and 1 is 
##example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
##example_data_categorical = ['ICU', 'death']
##example_data_groupby = ['death']

##example_data_labels={'death': 'mortality'}

##exampleTab1 = TableOne(example_data, columns=example_data_columns, categorical=example_data_categorical, groupby=example_data_groupby, rename=example_data_labels, pval=False)
##exampleTab1
##print(exampleTab1.tabulate(tablefmt = "fancy_grid"))


########################  ### load in the dataset 2



##my_data =pd.read_csv(r'data\SPARCS.csv')

df2 = my_data.copy()
list(df2)
df2.head(5)
df2.dtypes
df2['Patient Disposition']
df2['Emergency Department Indicator']
df2['Gender'].value_counts()
df2_columns= ['Age Group','Gender', 'Type of Admission','APR Risk of Mortality','Emergency Department Indicator','Patient Disposition','Health Service Area']


##df2_categorical = ['Age Group','APR Risk of Mortality','Gender','Health Service Area']       

df2_groupby = ['APR Risk of Mortality']
#or  df2_categorical = ['Age Group','APR Risk of Mortality','Gender','Health Service Area']   and  df2_groupby = ['Type of Admission']

df2_labels={'APR Risk of Mortality': 'Mortality'}
df2_table=TableOne(df2, columns=df2_columns, groupby=df2_groupby, rename=df2_labels, pval=False)
print(df2_table.tabulate(tablefmt = "fancy_grid"))
df2_table.to_csv('data\mytable.csv')


##################################

df2= pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

list(df2)
df2.head(5)
df2.dtypes
df2['patient_disposition']
df2['emergency_department_indicator']
df2['gender'].value_counts()
df2_columns= ['age_group','gender', 'type_of_admission','apr_risk_of_mortality','emergency_department_indicator','patient_disposition','health_service_area']
##df2_categorical = ['age_group','apr_risk_of_mortality','gender','health_service_area']       

df2_groupby = ['type_of_admission']
#or  df2_categorical = ['Age Group','APR Risk of Mortality','Gender','Health Service Area']   and  df2_groupby = ['apr_risk_of_mortality']

df2_labels={'apr_risk_of_mortality': 'Mortality'}
df2_table=TableOne(df2, columns=df2_columns, groupby=df2_groupby,rename=df2_labels, pval=False) 
print(df2_table.tabulate(tablefmt = "fancy_grid"))
df2_table.to_csv('data\mytable_1.csv')




###########################################


## Determining the column to split on :
import pandas 

income = pandas.read_csv('income.csv')


def find_best_column(data, target_name, columns):
    # Fill in the logic here to automatically find the columns to split on
    # Data is a dataframe
    # Target_name is the same of the target variable
    # Columns is a list of potential column to on 
    return None
# A list of columns to potentially split income with 
columns = ['age', 'workclass', 'education_num', 'marital_status','occupation','relationship','race','sex','hours_per_week','native_country']
def find_best_columns(data,target_name, columns):
    information_gains = []
    # Loop through and compute information gains :
    for col in columns: 
        information_gain = calc_information_gain(data,col, 'high_income')
        information_gains.append(information_gain)
    
    # Find the name of the columns with the highest gain : 
    highest_gain_index = information_gains.index(max(information_gain))
    highest_gain = columns[highest_gain_index]
    return highest_gain

income_split = find_best_column(income, 'high_income', columns)
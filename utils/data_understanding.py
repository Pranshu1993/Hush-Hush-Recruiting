import pandas as pd
from IPython.display import display


def simple_eda(df):
    """
    This function will feature the following parameters about the data:
    -Number of Rows
    -Number of Columns
    -Columns with missing values + Number of missing values
    -Number of Categorical Columns + a describe function for these columns
    -Number of Numerical or Continuous Columns + a describe function for these columns
    -Number of duplicated Rows
    """
    # Applying info() method
    print('---')
    print('Common information')
    print('---')
    print(df.info())

    # Number of Rows and Columns
    print('---\nNumber of rows: {}'.format(df.shape[0]))
    print('Number of columns: {}'.format(df.shape[1]))
    print('---')

    # Columns with missing values + Number of missing values
    if df.columns.isna().sum() == 0:
        print('There are no missing values')
    else:
        print('Detected')
        display(df.columns.isna().sum())

    # Categorical Columns, how many there are and describe() function to those columns
    print('---\nCategorical Columns')
    print('Total: {}'.format(len(df.select_dtypes(include='object').columns)))
    display(df.select_dtypes('object').describe())

    # Numerical Columns or Continuous Columns
    print('---\nNumerical Columns/Continuous Columns')
    print('Total: {}'.format(len(df.select_dtypes(include=['int64', 'float', 'int']).columns)))
    display(df.select_dtypes('int64' and 'float' and 'int').describe())

    # Checking for duplicated rows
    if df.duplicated().sum() == 0:
        print('---')
        print('There are no duplicates')
        print('---')
    else:
        print('---')
        print('Duplicates found')
        print('---')
        display(df[df.duplicated()])

    print()
    print('---')
    print('End of the report')
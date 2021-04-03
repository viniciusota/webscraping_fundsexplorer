import pandas as pd
import numpy as np
from decimal import Decimal


def preprocessing_values_column(column_name):
    data[column_name] = data[column_name].str.replace('.', '')
    data[column_name] = data[column_name].str.replace(',', '.')
    data[column_name] = data[column_name].str.replace(" ", '')
    data[column_name] = data[column_name].str.replace("R", '')
    data[column_name] = data[column_name].str.replace("$", '')
    data[column_name] = data[column_name].astype("float")
    return data[column_name]


def preprocessing_percent_columns(column_name):
    data[column_name] = data[column_name].str.replace("%", "")
    data[column_name] = data[column_name].str.replace(",", ".")
    data[column_name] = data[column_name].astype("float")
    data[column_name] = data[column_name]/100
    return data[column_name]


if __name__ == '__main__':
    data = pd.read_csv('DataSet_Fii.csv')
    for column_name in data.drop(['codigodofundo', 'setor'], axis=1).select_dtypes(['object']).columns:
        if data[column_name].str.contains('%').sum() > 0:
            data[column_name] = preprocessing_percent_columns(column_name=column_name)

        elif data[column_name].str.contains("$").sum() > 0:
            data[column_name] = preprocessing_values_column( column_name = column_name)
    data.to_csv("DataSet_Fii_preprocessed.csv",index=False)
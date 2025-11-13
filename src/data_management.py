import pandas as pd

# TODO get all data
def get_data():
    print("Getting data")

    df = pd.read_csv('../resources/data/data_2025.csv')

    return df
    
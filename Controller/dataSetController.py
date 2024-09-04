import pandas as pd
from datetime import datetime

data = pd.read_csv('DataSets\FIFA23_official_data.csv')

# Convert 'Contract Valid Until' to integers
data['Contract Valid Until'] = pd.to_numeric(data['Contract Valid Until'], errors='coerce')

# Function to convert value strings to numeric
def convert_value(value):
    if isinstance(value, str):
        value = value.replace('£', '').replace('€', '').replace('M', 'e6').replace('K', 'e3')
        try:
            return float(value)
        except ValueError:
            return None
    return value

# Apply the conversion function to the 'Value' column
data['Value'] = data['Value'].apply(convert_value)


data = data[data["Contract Valid Until"] >= datetime.today().year]
data = data[data["Value"] > 0]
data = data.sort_values(by="Overall", ascending=False)

def GetData():
    return data

def GetClubs():
    return data["Club"].value_counts().index
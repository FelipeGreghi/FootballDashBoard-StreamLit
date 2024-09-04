import pandas as pd
from datetime import datetime
import re

data = pd.read_csv('DataSets\FIFA23_official_data.csv')

# Convert 'Contract Valid Until' to integers
data['Contract Valid Until'] = pd.to_numeric(data['Contract Valid Until'], errors='coerce')

# Remove number to colum 'Name'
data['Name'] = data['Name'].str.replace(r'\d+', '', regex=True)

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

def GetPlayersByClub(club):
    dataPlayers = data[data["Club"] == club]
    players = dataPlayers["Name"].value_counts().index
    return players

def GetPlayerStats(player):
    playerStats = data[data["Name"] == player].iloc[0].copy()
    
    # Ensure 'Height' is a string, remove 'cm', and convert to meters
    playerStats['Height'] = str(playerStats['Height']).replace('cm', '')
    playerStats['Height'] = float(playerStats['Height']) / 100
    playerStats['Position'] = re.sub(r'<[^>]*>', '', playerStats['Position'])

    playerStats['Wage'] = convert_value(playerStats['Wage'],1000)
    playerStats['Release Clause'] = convert_value(playerStats['Release Clause'])
    
    return playerStats

def GetTeamStats(club):
    dataPlayers = data[data["Club"] == club].set_index("Name")
    return dataPlayers


def convert_value(value_str, multiplier=1):
        match = re.search(r'(\d+)', value_str)
        if match:
            return int(match.group(1)) * multiplier
        return 0
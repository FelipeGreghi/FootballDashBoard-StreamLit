import streamlit as st
import Controller.dataSetController as dataController

st.set_page_config(page_title="Players", page_icon=":soccer:", layout="wide")

# Sidebar
st.sidebar.title("Player Stats")
st.sidebar.subheader("Select Club and Player")

clubSelect = st.sidebar.selectbox("Club",dataController.GetClubs())

playerSelect = st.sidebar.selectbox("Player",dataController.GetPlayersByClub(clubSelect))

playerStats = dataController.GetPlayerStats(playerSelect)

st.image(playerStats['Photo'])
st.title(playerStats['Name'])

st.markdown(f"**Club:** {playerStats['Club']}")
st.markdown(f"**Position:** {playerStats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Age:** {playerStats['Age']}")
col2.markdown(f"**Height:** {playerStats['Height']}m")
col3.markdown(f"**Weight:** {playerStats['Weight']}")

st.divider()
st.subheader(f"Overall {playerStats['Overall']}")
st.progress(int(playerStats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Market Value", value=f"€ {int(playerStats['Value']):,}")
col2.metric(label="Wage", value=f"€ {int(playerStats['Wage']):,}")
col3.metric(label="Release Clause", value=f"€ {int(playerStats['Release Clause']):,}")


import streamlit as st
import Controller.dataSetController as dataController

st.set_page_config(page_title="Teams", page_icon=":soccer:", layout="wide")


# Sidebar
st.sidebar.title("Team Stats")
st.sidebar.subheader("Select Club")

clubSelect = st.sidebar.selectbox("Club",dataController.GetClubs())

teamStats = dataController.GetTeamStats(clubSelect)
st.image(teamStats['Club Logo'].iloc[0])
st.markdown(f"## {clubSelect}")

columns = ["Age", "Photo", "Flag", "Overall", "Value", "Wage", "Height", "Contract Valid Until", "Weight", "Release Clause"]

st.dataframe(teamStats[columns], 
             column_config={
                            "Flag": st.column_config.ImageColumn("Country"),
                            "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                            "Photo": st.column_config.ImageColumn("Photo"),
                            })

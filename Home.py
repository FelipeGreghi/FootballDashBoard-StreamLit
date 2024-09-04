import streamlit as st
import Controller.dataSetController as dataController

st.set_page_config(page_title="Home", page_icon=":home:", layout="wide")

st.title("Football Data Analysis")
st.markdown("""
Welcome to the Football Data Analysis application. This project provides an in-depth analysis of football players and clubs. 
You can explore various statistics, compare player performances, and gain insights into different clubs. 
Use the sidebar to navigate through the application and discover detailed information about your favorite players and teams.
""")
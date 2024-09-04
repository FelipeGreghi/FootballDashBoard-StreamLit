import streamlit as st
import Controller.dataSetController as dataController

st.title('2 Players')
st.write(dataController.GetClubs())

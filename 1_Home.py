import streamlit as st
import Controller.dataSetController as dataController

st.title('Home')

st.write(dataController.GetData())


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Product Intelligent")
st.sidebar.title("Inventory")

st.markdown("Product Intelligent ")
st.sidebar.markdown("Inventory And Product Performance")


DATA_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vShThnh_A7EQokSMvs1MKzDDzpZp13tOI2d9AjSGoxYgVYOcpgkwqhQD0tQT5pR8M3gOx7YZn9lS4Tr/pub?gid=1172464903&single=true&output=csv")
#DATA_URL_1 = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vShThnh_A7EQokSMvs1MKzDDzpZp13tOI2d9AjSGoxYgVYOcpgkwqhQD0tQT5pR8M3gOx7YZn9lS4Tr/pub?gid=995490562&single=true&output=csv")
#st.DATA_URL
#data=load
st.write(DATA_URL)
#Bar Chart
#st.bar_chart(DATA_URL["Reach"])
#st.bar_chart(DATA_URL["Platform"])

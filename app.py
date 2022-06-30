import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown("Product Intelligent ")
st.sidebar.markdown("Inventory And Product Performance")


DATA_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vShThnh_A7EQokSMvs1MKzDDzpZp13tOI2d9AjSGoxYgVYOcpgkwqhQD0tQT5pR8M3gOx7YZn9lS4Tr/pub?gid=1172464903&single=true&output=csv")
#DATA_URL_1 = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vShThnh_A7EQokSMvs1MKzDDzpZp13tOI2d9AjSGoxYgVYOcpgkwqhQD0tQT5pR8M3gOx7YZn9lS4Tr/pub?gid=995490562&single=true&output=csv")
st.bar_chart(DATA_URL)

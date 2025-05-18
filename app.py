import requests
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from client import STOCK_API



# give page name


st.set_page_config(page_title= "STOCK MARKET APP" , layout= 'wide')




# add page title

st.title("Stock Market App")

# add subheading 

st.subheader("by Varsha Mhetre")

# add company

company = st.time_input("company name" : str)
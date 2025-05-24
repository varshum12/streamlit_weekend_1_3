import streamlit as st
from client import STOCK_API
import plotly.graph_objects  as go


# Set title to page

st.set_page_config(page_title= 'Stock Market  app' , layout= 'wide')

# give title inside page 

st.title("STOCK MARKET APP")

st.subheader('By Varsha Mhetre')


# add text box for company name

company =  st.text_input("Enter company name")

# creat connection between backend and frontend

@st.cache_resource(ttl =  3600)
def fetch_data():
    return STOCK_API(api_key= st.secrets['API_KEY'])

stock_api  =  fetch_data()

# create class for get symbol
st.cache_data(ttl =  3600)
def get_symbol(company_name):
    return stock_api.symbol_search(company_name)

# Plot the graph 

@st.cache_data(ttl =  3600)
def graph(symbol):
    df  = stock_api.daily_data(symbol)
    fig  =  stock_api.plot_chart(df)
    return fig


if company:


# if compnay exists
    company_data  = get_symbol(company_name=company)
    if company_data :
    
        symbols_data  =  list(company_data.keys())

        options     =  st.selectbox("search symbol here" , symbols_data)
        selected_data =  company_data[options]
        st.success(f"company name {selected_data[0]}")
        st.success(f"company Region  {selected_data[1]} ")

        st.success(f"currency {selected_data[2]}")

        submit =  st.button('Plot'  ,type =  "primary")
        if submit :
            fig  = graph(symbol=options)
            st.plotly_chart(fig , use_container_width= True)
    else:
        st.warning('Company is not exists')

        













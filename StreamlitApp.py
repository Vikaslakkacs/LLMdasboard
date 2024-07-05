import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


## Page configuration
st.set_page_config(
    page_title= "Application Monitoring",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")


#############################
#side bar
with st.sidebar:
    st.title("Application Monitoring")
    year_list= [2024, 2023, 2022, 2021]
    selected_year= st.selectbox('Select a year', year_list)
    
    ##Selecting Color theme
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
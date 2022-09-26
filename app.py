import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


df = pd.read_parquet('beta.parquet.gzip') 

st.write(df)

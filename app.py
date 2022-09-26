import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

df = pd.read_parquet('beta.parquet.gzip') 

st.write(df)

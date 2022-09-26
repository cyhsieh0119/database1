import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

df = pd.read_parquet('beta.parquet.gzip') 

grid_options = {
    "columnDefs": [
        {
            "headerName": "col1,
            "field": "col1",
            "editable": True,
        },
        {
            "headerName": "col2",
            "field": "col2",
            "editable": False,
        },
    ],
}

grid_return = AgGrid(df, grid_options)
new_df = grid_return["data"]

st.write(new_df)


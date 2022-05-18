# // Draw a line chart

import streamlit as st 
import numpy as np 
import pandas as pd

st.title("# Draw a line chart")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)

st.dataframe(chart_data)

st.line_chart(chart_data)
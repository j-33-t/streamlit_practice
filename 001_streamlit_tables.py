import streamlit as st 
import numpy as np
import pandas as pd

st.write("# Display DataFrame")



# // st.write : Write arguments to the app
st.title("St.write")

st.write(pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
}))

# // method for interactive table generation
st.title("St.dataframe")
st.write("interactive table generation")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


# // Method for static table generation
st.title("St.Table")
st.write("static table generation")
dataframe = pd.DataFrame(
    np.random.randn(10, 12),
    columns=('col %d' % i for i in range(12)))
st.table(dataframe)


# // Checkboxes to show and hide data

st.title("Checkbox to display Data")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
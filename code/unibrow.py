'''
Solution unibrow.py
'''

# Upload a file using Streamlit, accepting files of types .csv, .xlsx, and .json. 
# Get the file extension of the uploaded file to determine its type and load the file accordingly. 
#Retrieve all column names from the loaded dataframe and allow the user to select which columns to display using a multi-select widget, with all columns selected by default. 
# Provide an option to toggle data filtering, which enables the user to filter the dataframe by selecting a specific value from text-based columns. 
# Display the filtered or unfiltered dataframe using Streamlit, along with a statistical summary of the numerical columns.

import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file", type=['csv', 'json', 'xlsx'])
if file:
    file_type = pl.get_file_extension(file.name)
    file_df = pl.load_file(file, file_type)
    cols = pl.get_column_names(file_df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    if st.toggle("Filter data"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(file_df, 'object')
        filter_col = stcols[0].selectbox("Select column to filter", text_cols)
        if filter_col:
            vals = pl.get_unique_values(file_df, filter_col)
            val = stcols[1].selectbox("Select value to filter On", vals)
            file_df_show = file_df[file_df[filter_col] == val][selected_cols]
    else:
        file_df_show = file_df[selected_cols]
    st.dataframe(file_df_show)
    st.dataframe(file_df_show.describe())



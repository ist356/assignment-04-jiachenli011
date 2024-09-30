'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file", type=['csv', 'json', 'xlsx'])
if file:
    file_type = pl.get_file_extension(file.name)
    file_df = pl.load_file(file, file_type)
    



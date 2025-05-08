import pandas as pd
import streamlit as st


def load_csv(uploaded_file, resource_names, obj_name):
    df = pd.read_csv(uploaded_file)
    cols = ['Produto','Tipo',obj_name] + resource_names
    if not all(c in df.columns for c in cols):
        st.error(f"CSV deve conter {cols}")
        st.stop()
    df = df[cols].copy()
    if 'Min' not in df: df['Min'] = 0.0
    if 'Max' not in df: df['Max'] = float('inf')
    df[['Min','Max']+resource_names+[obj_name]] = df[['Min','Max']+resource_names+[obj_name]].apply(pd.to_numeric)
    return df
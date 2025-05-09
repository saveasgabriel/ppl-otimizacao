import streamlit as st
from components.sidebar import render_sidebar
from components.table_editor import render_table_editor
from components.results_display import display_results
from model.builder import build_model
from model.solver import solve_model
from utils.io import load_csv

st.set_page_config(page_title="Otimização Linear", layout="wide")
st.title("Otimização com Programação Linear")

# Lado esquerdo: inputs e configurações
config = render_sidebar()

# Carrega dados
if config['uploaded_file']:
    df = load_csv(config['uploaded_file'], config['resource_names'], config['obj_name'])
else:
    df = None

# Editor de tabela
prod_df = render_table_editor(df, config)

# Ao clicar em resolver
if st.button("Resolver"):
    model = build_model(prod_df, config)
    result, sol_series, usage_df, obj_val = solve_model(model, config['solver'], prod_df, config)
    display_results(result, sol_series, usage_df, config['obj_name'], obj_val)
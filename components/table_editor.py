import streamlit as st
import pandas as pd

def editable_df(df, key, column_config=None):
    if hasattr(st, 'data_editor'):
        return st.data_editor(df, num_rows='dynamic', column_config=column_config or {}, key=key)
    else:
        return st.experimental_data_editor(df, num_rows='dynamic', column_config=column_config or {}, key=key)


def render_table_editor(df, config):
    obj = config['obj_name']
    resources = config['resource_names']

    if df is None:
        # criar df padrão
        data = {
            'Produto': [f'P{i+1}' for i in range(config['n_prod'])],
            'Tipo': ['Contínua'] * config['n_prod'],
            obj: [0.0] * config['n_prod'],
            'Min': [0.0] * config['n_prod'],
            'Max': [float('inf')] * config['n_prod']
        }
        for r in resources:
            data[r] = [0.0] * config['n_prod']
        df = pd.DataFrame(data)

    # Configurações de coluna
    config_cols = {
        'Produto': st.column_config.TextColumn('Produto'),
        'Tipo': st.column_config.SelectboxColumn('Tipo', options=['Contínua','Inteira']),
        obj: st.column_config.NumberColumn(obj, min_value=0.0),
        'Min': st.column_config.NumberColumn('Min', min_value=0.0),
        'Max': st.column_config.NumberColumn('Max', min_value=0.0),
    }
    for r in resources:
        config_cols[r] = st.column_config.NumberColumn(r, min_value=0.0)

    return editable_df(df, key='prod_editor', column_config=config_cols)
import streamlit as st
import pandas as pd

def display_results(result, sol_series, usage_df, obj_name, obj_val):
    from pyomo.opt import TerminationCondition
    if result.solver.termination_condition == TerminationCondition.optimal:
        st.success('Solução ótima encontrada')
        st.dataframe(sol_series.to_frame('Quantidade'))
        st.metric(obj_name, f"{obj_val:.2f}")

        st.subheader('Uso de Recursos')
        st.dataframe(usage_df)

        csv = sol_series.to_frame().to_csv().encode('utf-8')
        st.download_button('Baixar CSV', csv, 'resultado.csv', 'text/csv')
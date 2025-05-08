import streamlit as st
import pandas as pd

def display_results(result, sol_series, usage_df, obj_name):
    from pyomo.opt import TerminationCondition
    if result.solver.termination_condition == TerminationCondition.optimal:
        st.success('Solução ótima encontrada')
        st.dataframe(sol_series.to_frame('Quantidade'))
        st.metric(obj_name, f"{sol_series.name:.2f}")

        st.subheader('Uso de Recursos')
        st.dataframe(usage_df)

        csv = sol_series.to_frame().to_csv().encode('utf-8')
        st.download_button('Baixar CSV', csv, 'resultado.csv', 'text/csv')
    elif result.solver.termination_condition == TerminationCondition.infeasible:
        st.error('Problema inviável')
    else:
        st.error('Nenhuma solução ótima encontrada')
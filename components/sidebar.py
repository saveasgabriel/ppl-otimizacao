import streamlit as st

def render_sidebar():
    st.sidebar.header("Configurações")
    opt_type = st.sidebar.selectbox("Tipo de Otimização", ["Maximização", "Minimização"])
    obj_name = st.sidebar.text_input("Nome da Função Objetivo", value="Lucro")
    n_prod = st.sidebar.number_input("Número de Produtos", min_value=1, value=3)
    n_rec = st.sidebar.number_input("Número de Recursos", min_value=1, value=2)
    demanda_min = st.sidebar.number_input("Demanda Mínima Total (∑ x ≥)", min_value=0.0, value=0.0)
    demanda_max = st.sidebar.number_input("Demanda Máxima Total (∑ x ≤)", min_value=0.0, value=100.0)
    solver = st.sidebar.selectbox("Solver", ["glpk"])
    uploaded = st.sidebar.file_uploader("Importar CSV", type=["csv"])

    resources = []
    for i in range(n_rec):
        with st.sidebar.expander(f"Recurso {i+1}", expanded=(i==0)):
            name = st.text_input("Nome", key=f"rec{i}", value=f"R{i+1}")
            avail = st.number_input("Disponibilidade", min_value=0.0, value=100.0, key=f"disp{i}")
        resources.append((name, avail))
    resource_names = [r[0] for r in resources]
    disponibilidade = dict(resources)

    return {
        'opt_type': opt_type,
        'obj_name': obj_name,
        'n_prod': n_prod,
        'resource_names': resource_names,
        'disponibilidade': disponibilidade,
        'demanda_min': demanda_min,
        'demanda_max': demanda_max,
        'solver': solver,
        'uploaded_file': uploaded
    }
# Aplicativo de Otimização Linear (Modularizado)

Este repositório contém um aplicativo web para modelagem e solução de problemas de Programação Linear e Mista (MIP) com **Streamlit** e **Pyomo**, organizado de forma modular para facilitar manutenção e extensão.

---

## Estrutura de Pastas

```text
├── app.py                    # Ponto de entrada Streamlit
├── components/               # Componentes de interface (UI)
│   ├── sidebar.py            # Widgets da barra lateral
│   ├── table_editor.py       # Função de edição de tabela
│   └── results_display.py    # Exibição de resultados
├── model/                    # Construção e solução de modelos Pyomo
│   ├── builder.py            # Função que monta o ConcreteModel
│   └── solver.py             # Execução do solver e retorno de resultados
├── utils/                    # Utilitários e validações gerais
│   └── io.py                 # Importação e validação de CSV
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação principal (este arquivo)
```

---

## Funcionalidades

- **Configuração Interativa**  
  - Tipo de otimização (Maximização/Minimização)  
  - Definição de função objetivo (nome e coeficientes)  
  - Número de produtos e recursos  
  - Demanda total mínima e máxima  
  - Escolha de solver (GLPK)  

- **Gerenciamento de Dados**  
  - Importação de CSV com colunas obrigatórias e opcionais (Min/Max)  
  - Edição dinâmica da tabela de produtos via `st.data_editor`  
  - Definição de domínio contínuo ou inteiro para variáveis  

- **Modelagem e Solução**  
  - Construção automática de modelo Pyomo  
  - Inclusão de restrições de recursos, demanda e limites unitários  
  - Execução do solver com fallback automático  

- **Resultados**  
  - Exibição de quantidades ótimas e valor da função objetivo  
  - Relatório de uso de cada recurso  
  - Download da solução em CSV  

---

## Instalação

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/otimizacao-linear.git
   cd otimizacao-linear
   ```

2. Crie e ative uma venv (PowerShell):  
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Instale dependências:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

Execute o app:  
```bash
streamlit run app.py
```
Abra no navegador: `http://localhost:8501` e siga os passos:

1. Ajuste configurações na barra lateral.  
2. (Opcional) Importe um CSV pré-formatado.  
3. Edite ou confirme a tabela de produtos.  
4. Clique em **Resolver**.  
5. Visualize e baixe os resultados.


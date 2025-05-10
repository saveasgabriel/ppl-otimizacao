import pandas as pd
from pyomo.environ import SolverFactory, value

def solve_model(model, solver_name, df, config):
    solver = SolverFactory(solver_name)
    if not solver.available():
        solver = SolverFactory(solver_name)
    result = solver.solve(model)

    sol = {p: model.x[p]() for p in model.P}
    sol_series = pd.Series(sol, name='Quantidade')
    
    # extrair valor da função objetivo
    obj_val = value(model.obj)
    usage = {}
    for r in config['resource_names']:
        uso_r = df.set_index('Produto')[r].to_dict()
        usage[r] = sum(uso_r[p] * model.x[p]() for p in model.P)

    usage_df = pd.DataFrame(usage, index=['Uso']).T
    return result, sol_series, usage_df, obj_val
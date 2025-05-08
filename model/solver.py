from pyomo.environ import SolverFactory

def solve_model(model, solver_name):
    solver = SolverFactory(solver_name)
    if not solver.available():
        solver = SolverFactory(solver_name)
    result = solver.solve(model)

    # extrair solução e uso
    sol = {p: model.x[p]() for p in model.P}
    usage = {r: sum(model.x[p]()*model.x[p].parent_block().component_map()[r] for p in model.P) for r in model.P}  # ajustar conforme df
    import pandas as pd
    sol_series = pd.Series(sol, name='Quantidade')
    usage_df = pd.DataFrame(usage, index=['Uso']).T
    return result, sol_series, usage_df